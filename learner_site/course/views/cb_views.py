from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView, Response
from rest_framework.viewsets import ModelViewSet

from course.forms import CourseForm, StudentForm
from course.models import Course 
from people.models import Student

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
)

from ..serializers import CourseSerializer

class CreateStudentView(View):

    def get(self, request):
        form = StudentForm()
        return render(request, 'create_student.html', context={"form": form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'create_student.html', context={"form": form})


class DeleteCourseView(DeleteView):
    model = Course

    def get_success_url(self):
        return '/all_courses'


class UpdateCourseView(UpdateView):
    model = Course
    fields = '__all__'
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return '/course_detail/{}/'.format(self.object.pk)


class AllCoursesTemplateView(TemplateView):

    template_name = 'all_courses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courses = Course.objects.all()
        context.update({"courses": courses})

        return context


class AllStudentsTemplateView(TemplateView):

    template_name = 'all_students.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = Student.objects.all()
        context.update({"students": students})

        return context


class CourseDetailView(DetailView):

    model = Course


class StudentDetailView(DetailView):

    model = Student


class CourseCreateView(CreateView):

    model = Course
    fields = '__all__'
    success_url = '/all_courses/'

    def get_success_url(self):
        return '/course_detail/{}/'.format(self.object.pk)


class StudentCreateView(CreateView):

    model = Student
    fields = '__all__'
    success_url = '/all_students/'

    def get_success_url(self):
        return '/student_detail/{}/'.format(self.object.pk)


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
