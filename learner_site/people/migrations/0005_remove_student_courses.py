# Generated by Django 2.2.12 on 2020-06-12 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20200612_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
    ]