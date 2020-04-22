from django.forms import ModelForm
from .models import City, Course, Student


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
