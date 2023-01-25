from django.contrib import admin
from login.models import User
from lesson.models import Lesson
from user_profile.models import Profile
from lesson.models import Day
from schedule.models import Table
admin.site.register(User)
admin.site.register(Lesson)
admin.site.register(Profile)
admin.site.register(Day)
admin.site.register(Table)
# admin.site.register()
# Register your models here.
