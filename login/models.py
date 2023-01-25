from django.db import models
from django.shortcuts import render, redirect


class User(models.Model):
    username = models.CharField(max_length=255, null=False, blank=False, unique=True, default='')
    password = models.CharField(max_length=255, null=False, blank=False, default='')

    def register_attempt(request):
        new_user = User(username=request.POST['username'], password=request.POST['password'])
        new_user.save()

    def get_user(request):
        user_id = request.session.get('user_id')
        if user_id is not None:
            return User.objects.get(id=user_id)

    def __str__(self):
        return self.username

