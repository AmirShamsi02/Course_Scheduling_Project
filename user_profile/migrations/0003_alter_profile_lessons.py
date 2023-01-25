# Generated by Django 4.1.4 on 2022-12-31 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_remove_lesson_user'),
        ('user_profile', '0002_profile_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lessons',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lesson.lesson', unique=True),
        ),
    ]