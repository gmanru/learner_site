from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return HttpResponse('<h1>Hello django teacher panel</h1>')
# Create your views here.