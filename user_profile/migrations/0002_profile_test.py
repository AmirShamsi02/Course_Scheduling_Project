# Generated by Django 4.1.4 on 2022-12-31 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='test',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
