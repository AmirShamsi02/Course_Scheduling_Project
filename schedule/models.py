from django.db import models
from user_profile.models import Profile
from user_profile.models import User


# Create your models here.
class Table(models.Model):
    profile = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, related_name='profile_tables')

    def __str__(self):
        return self.profile.login_user.username

    def current_table(request):
        current_table = Table.objects.get(profile=User.get_user(request).profile)
        return current_table

    def create_table(request):
        if not Table.objects.filter(profile=User.get_user(request).profile).exists():
            new_table = Table(profile=User.get_user(request).profile)
            new_table.save()


