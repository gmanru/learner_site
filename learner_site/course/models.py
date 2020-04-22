from django.db import models

# Create your models here.


class City(models.Model):
    name = models.TextField()
    population = models.BigIntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.TextField()
    number = models.SmallIntegerField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name