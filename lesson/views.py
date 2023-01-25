from django.shortcuts import render, redirect
from django.http import HttpResponse
from lesson.models import Lesson
from user_profile.models import Profile
from login.models import User
from lesson.models import Day
from login.views import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import user_passes_test
from schedule.models import Table

weekdays = ['sat', 'sun', 'mon', 'tue', 'wed', 'thu']


def make_day(checkbox, lesson):
    if checkbox:
        day = Day(day=checkbox, lesson=lesson)
        day.save()
        return True
    return False


def fillment_error(input_vals):
    inputs = ["name", "code", "teacher", "credit"
        , "Exam_D", "time"]
    error = ""
    for i in range(6):
        if input_vals[i]:
            continue
        error += f" , {inputs[i]}"
    return error


@require_http_methods(request_method_list=['POST', 'GET'])
@login_required
def insert(request):
    error = None

    course_name = request.POST.get('name', False)
    course_user_profile = User.get_user(request).profile
    course_code = request.POST.get('code', False)
    course_teacher = request.POST.get('teacher', False)
    course_credit = request.POST.get('credit', False)
    course_Exam_D = request.POST.get('exam_date', False)
    course_time = request.POST.get('time_days', False)

    form_val = [course_name, course_code,
                course_teacher, course_credit, course_Exam_D,
                course_time
                ]

    error = fillment_error(form_val)
    if len(error) != 0:
        return render(request, 'lesson/Insertion_page.html', {'error': error})

    lesson = Lesson(
        profile=course_user_profile, name=course_name, code=course_code,
        teacher=course_teacher, class_hour=course_time, credits=course_credit,
        exam_date=course_Exam_D
    )
    lesson.save()

    flag = True
    for i in range(6):
        checkbox = request.POST.get(weekdays[i] + 'box', False)
        check = make_day(checkbox, lesson)
        if check:
            flag = False

    if flag:
        error = "حداقل یک روز را انتخاب نمایید"
        lesson.delete()
        return render(request, 'lesson/Insertion_page.html', {'error': error})

    return redirect('scheduler:user_lessons_list')
#return render(request, 'lesson/Insertion_page.html')
