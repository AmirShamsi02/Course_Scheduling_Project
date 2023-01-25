from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.http import HttpResponse
from lesson.models import Lesson, Day
from login.models import User
from login.views import login_required, logout
from schedule.models import Table

Weekdays = (
    ('0', 'Sat'), ('1', 'Sun'), ('2', 'Mon'),
    ('3', 'Tue'), ('4', 'Wed'), ('5', 'Thu')
)

Hours = (
    ('1', '7_9'),
    ('2', '9_11'),
    ('3', '11_13'),
    ('4', '13_15'),
    ('5', '15_17'),
    ('6', '17_19'),
    ('7', '19_21')
)

hours = {
    '1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6
}

weekdays = {
    'sat': 0, 'sun': 1, 'mon': 2, 'tue': 3, 'wed': 4, 'thu': 5
}

vars = [['sat_a', 'sat_b', 'sat_c', 'sat_d', 'sat_e', 'sat_f', 'sat_g'],
        ['sun_a', 'sun_b', 'sun_c', 'sun_d', 'sun_e', 'sun_f', 'sun_g'],
        ['mon_a', 'mon_b', 'mon_c', 'mon_d', 'mon_e', 'mon_f', 'mon_g'],
        ['tue_a', 'tue_b', 'tue_c', 'tue_d', 'tue_e', 'tue_f', 'tue_g'],
        ['wed_a', 'wed_b', 'wed_c', 'wed_d', 'wed_e', 'wed_f', 'wed_g'],
        ['thu_a', 'thu_b', 'thu_c', 'thu_d', 'thu_e', 'thu_f', 'thu_g']]


@login_required
def list(request):
    lessons = Lesson.objects.filter(profile__login_user=User.get_user(request))
    error = None
    context = {'lessons': lessons, 'username': User.get_user(request), 'errors': error}

    if request.method == 'POST':
        if request.POST.get('logout'):
            return logout(request)

        lesson_code = request.POST.get('lessons_list', False)

        lesson = Lesson.objects.get(code=lesson_code)

        if request.POST.get('add-button'):  # adding lesson to the table when + is clicked
            add_lesson(request, lesson)
            context.update({'errors': exam_day_collision(request)})
            context = fill_context(request, context)
            return render(request, 'schedule/Schedule_page.html', context)

        if request.POST.get('remove-button'):
            if not lesson.table is None:  # removing lesson to the table when - is clicked
                remove_lesson(request, lesson)
                context.update({'errors': exam_day_collision(request)})
                context = fill_context(request, context)
                return render(request, 'schedule/Schedule_page.html', context)

    context.update({'errors':exam_day_collision(request)})
    context = fill_context(request, context)

    return render(request, 'schedule/Schedule_page.html', context)


def exam_day_collision(request):  # returns a list of founded collision lessons
    errors = []
    table_lessons_list = Lesson.objects.filter(table=Table.current_table(request))

    for i in range(len(table_lessons_list)):
        for j in range(i + 1, len(table_lessons_list)):
            if table_lessons_list[i].exam_date == table_lessons_list[j].exam_date:
                errors.append("در یک زمان می باشد" + f" {table_lessons_list[i].name} " + "با درس" + f" {table_lessons_list[j].name} " + "امتحان درس")
    return errors

def class_day_collision(request, selected_lesson):
    collisions = []  # a list of positions which should have more than  one lesson
    times = find_position(selected_lesson)
    table_lessons = Lesson.objects.filter(table=Table.current_table(request))
    for table_lesson in table_lessons:
        table_lesson_times = find_position(table_lesson)
        collisions += intersection(table_lesson_times, times)

    return collisions


def find_position(lesson):  # gives a list of vars related to the lesson's position on the table
    day_vars = []
    days = Day.objects.filter(lesson=lesson)
    time_j = hours[lesson.class_hour]
    for i in range(len(days)):
        day_i = weekdays[days[i].day]
        day_vars.append(vars[day_i][time_j])

    return day_vars


def fill_context(request, context):
    table_lessons = Lesson.objects.filter(table=Table.current_table(request))
    for table_lesson in table_lessons:
        positions = find_position(table_lesson)
        for position in positions:
            exists = context.setdefault(position, False)
            if exists:
                pre_lessons = exists
                pre_lessons.append(table_lesson)
                context.update({position: pre_lessons})

            else:
                context.update({position: [table_lesson]})
    return context


def add_lesson(request, lesson):
    lesson.table = Table.current_table((request))
    lesson.save()
    return


def remove_lesson(request, lesson):
    lesson.table = None
    lesson.save()
    return


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
