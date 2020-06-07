from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView, Response
from rest_framework.viewsets import ModelViewSet
from .models import Student, Teacher


from .serializers import StudentSerializer, TeacherSerializer

from django.contrib.auth.models import User, Group

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
)

from oauth2_provider.contrib.rest_framework import (
    TokenHasReadWriteScope,
    TokenHasScope,
)

from .serializers import UserSerializer, GroupSerializer


class UserList(ListCreateAPIView):
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(ListAPIView):
    permission_classes = [IsAuthenticated, TokenHasScope]
    required_scopes = ["groups"]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
