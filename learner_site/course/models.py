from django.db import models


class City(models.Model):
    name = models.TextField()
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.TextField()
    number = models.SmallIntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class StudentInCources(models.Model):
    name = models.CharField(max_length=50)
    student = models.ForeignKey('people.Student', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

