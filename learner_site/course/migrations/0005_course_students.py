# Generated by Django 2.2.12 on 2020-06-12 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20200605_1951'),
        ('course', '0004_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='people.Student'),
            preserve_default=False,
        ),
    ]