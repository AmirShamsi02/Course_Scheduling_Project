from django.db import models
from login.models import User


class Profile(models.Model):
    login_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def login_attempt(request):
        if not Profile.objects.filter(login_user=User.get_user(request)).exists():
            new_profile = Profile(login_user=User.get_user(request))
            new_profile.save()

    def __str__(self):
        return self.login_user.username
    # Create your models here.
