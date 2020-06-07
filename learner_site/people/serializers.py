from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Student, Teacher


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "id", "username", "email", "first_name", "last_name",


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "id", "name",


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = 'id', 'first_name', 'email'
        view_name = 'student'


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = 'id', 'full_name', 'email'
        view_name = 'teacher'
