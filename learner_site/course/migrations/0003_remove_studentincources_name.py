# Generated by Django 2.2.12 on 2020-06-02 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_studentincources'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentincources',
            name='name',
        ),
    ]
