# Generated by Django 2.2.12 on 2020-06-12 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_course_students'),
        ('people', '0003_auto_20200605_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='members',
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.Course'),
        ),
    ]
