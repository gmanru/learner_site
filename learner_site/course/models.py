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
    students = models.ForeignKey('people.Student', on_delete=models.CASCADE)
    teachers = models.ForeignKey('people.Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StudentInCources(models.Model):
    student = models.ForeignKey('people.Student', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    @property
    def link(self):
        return f"  {self.course}"

    def __str__(self):
        return self.link
