from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(null=True)
    email = models.EmailField()
    course = models.ManyToManyField('course.Course', related_name="course")
    """members = models.ManyToManyField(
        'course.Course',
        through='course.StudentInCources',
        through_fields=('student', 'course'),
    ) для дальнейшей связи с mtm моделью """ 

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
