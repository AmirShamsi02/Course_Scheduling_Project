# Generated by Django 4.1.4 on 2023-01-21 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0013_alter_lesson_class_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='class_date',
            field=models.CharField(choices=[('1', 'Sat'), ('2', 'Sun'), ('3', 'Mon'), ('4', 'Tue'), ('5', 'Wed'), ('6', 'Thu')], default='', max_length=11),
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('1', 'Sat'), ('2', 'Sun'), ('3', 'Mon'), ('4', 'Tue'), ('5', 'Wed'), ('6', 'Thu')], default='', max_length=1)),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='day', to='lesson.lesson')),
            ],
        ),
    ]
