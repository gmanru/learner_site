"""learner_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import course.views.cb_views as class_based_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teacher/', include('teacher.urls')),
    path('student/', include('student.urls')),

    path('all_courses/', class_based_views.AllCoursesTemplateView.as_view()),
    path('course_create/', class_based_views.CourseCreateView.as_view()),
    path('course_detail/<int:pk>/', class_based_views.CourseDetailView.as_view()),
    path('course_delete/<int:pk>/', class_based_views.DeleteCourseView.as_view()),
    path('course_update/<int:pk>/', class_based_views.UpdateCourseView.as_view()),
    
    path('cb_create_student/', class_based_views.CreateStudentView.as_view()),
    path('all_students/', class_based_views.AllStudentsTemplateView.as_view()),
    path('student_detail/<int:pk>/', class_based_views.AllStudentsTemplateView.as_view()),
    path('cb_student_create/', class_based_views.StudentCreateView.as_view()),

]
