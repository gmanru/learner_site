from django.contrib import admin
from django.urls import path, include
import course.views.cb_views as class_based_views
from graphene_django.views import GraphQLView
from .schema import schema
from app.views import ContactFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('people/', include('people.urls')),

    path('all_courses/', class_based_views.AllCoursesTemplateView.as_view()),
    path('course_create/', class_based_views.CourseCreateView.as_view()),
    path('course_detail/<int:pk>/', class_based_views.CourseDetailView.as_view()),
    path('course_delete/<int:pk>/', class_based_views.DeleteCourseView.as_view()),
    path('course_update/<int:pk>/', class_based_views.UpdateCourseView.as_view()),
    
    path('contacts', ContactFormView.as_view()),

    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
    
    path('cb_create_student/', class_based_views.CreateStudentView.as_view()),
    path('all_students/', class_based_views.AllStudentsTemplateView.as_view()),
    path('student_detail/<int:pk>/', class_based_views.AllStudentsTemplateView.as_view()),
    path('cb_student_create/', class_based_views.StudentCreateView.as_view()),

]
