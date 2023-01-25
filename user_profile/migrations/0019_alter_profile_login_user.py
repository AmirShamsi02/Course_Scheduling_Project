# Generated by Django 4.1.4 on 2023-01-21 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_remove_user_last_login'),
        ('user_profile', '0018_alter_profile_login_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='login_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='login.user'),
        ),
    ]
