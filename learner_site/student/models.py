from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Course(models.Model):
    '''TTR_L_1 = 1
    TTR_1_5 = 2
    TTR_10 = 3
    TTR_12 = 4
    TTR_24 = 5'''

    TIME_TO_LEARN = (
        (1, '< 1 month'),
        (2, '5 month'),
        (3, '10 month'),
        (4, '1 year'),
        (5, '> 2 year'),
    )

    title = models.CharField(max_length=254)
    text = models.TextField()
    time_to_learn = models.IntegerField(choices=TIME_TO_LEARN)
    ts_last_changed = models.DateTimeField(auto_now=True)
    ts_created = models.DateTimeField(auto_now_add=True)

    student = models.ForeignKey(Student, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
