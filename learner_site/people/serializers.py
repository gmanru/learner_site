from rest_framework import serializers

from .models import Student, Teacher


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
        # exclude =
    # id = serializers.IntegerField()
    # title = serializers.CharField()
    # done = serializers.BooleanField()
    # author = AuthorSerializer()