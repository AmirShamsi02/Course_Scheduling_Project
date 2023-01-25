from django.shortcuts import render, redirect
from django.http import HttpResponse
from login.models import User
from user_profile.models import Profile
from django.views.decorators.http import require_http_methods
from schedule.models import Table


# Create your views here
def fillment_check(inputs):  # merge
    error = ""
    inputs_order = ["'نام کاربری'", "'رمز عبور'"]
    for i in range(2):
        if inputs[i]:
            continue
        error += " " + inputs_order[i]

    return error


def login(request):
    error = ""  # merge
    if request.method == 'POST':
        # merge/
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        # merge/

        inputs_val = [username, password]  # merge

        if User.objects.filter(username=username, password=password).exists():
            user = User.objects.get(username=username, password=password)
            request.session['user_id'] = user.id
            Profile.login_attempt(request)
            Table.create_table(request)
            return redirect('scheduler:user_lessons_list')

            # merge/
        error = fillment_check(inputs_val)
        if len(error) != 0:
            error = "لطفا" + f"{error}" + " را وارد نمایید"
            return render(request, 'login/login_page.html', {"error": error})

        error = "نام کاربری یا رمز عبور اشتباه می باشد."
        # merge/

    return render(request, 'login/login_page.html', {"error": error})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        inputs_val = [username, password]
        error = fillment_check(inputs_val)
        if len(error) != 0:
            error = "لطفا" + f"{error}" + " را وارد نمایید"
            return render(request, 'login/signup_page.html', {"error": error})

        if User.objects.filter(username=username).exists():
            error = "این نام کاربری تکراری است."
            return render(request, 'login/signup_page.html', {"error": error})

        User.register_attempt(request)
        return redirect('login:login')
    return render(request, 'login/signup_page.html')


def direct(request):
    return redirect('login:login')


def login_required(function):
    def wrapper(request, login_url='login:login', *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect(login_url)
        else:
            return function(request, *args, **kwargs)

    return wrapper


def logout(request):
    del request.session['user_id']
    return redirect('login:login')

