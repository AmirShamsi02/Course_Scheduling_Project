from django.db import models
from user_profile.models import Profile
from schedule.models import Table
SEMESTER_CHOICES = (  # Credits choices
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)

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


class Lesson(models.Model):
    profile = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, related_name='lessons')
    table = models.ForeignKey(Table, null=True, on_delete=models.CASCADE, related_name='table_lessons')
    code = models.CharField(max_length=255)
    class_hour = models.CharField(max_length=1, choices=Hours, default='')
    exam_date = models.DateTimeField()
    name = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    credits = models.CharField(max_length=1, choices=SEMESTER_CHOICES)

    def __str__(self):
        return self.name + ' ' + self.code[-2] + self.code[-1]


class Day(models.Model):
    day = models.CharField(max_length=1, choices=Weekdays, default='')
    lesson = models.ForeignKey(Lesson, null=True, on_delete=models.CASCADE, related_name='days')

    def __str__(self):
        return self.day + ' ' + self.lesson.name
