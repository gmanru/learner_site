# Generated by Django 2.2.12 on 2020-06-07 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_remove_studentincources_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
