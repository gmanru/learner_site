from django.urls import path, include


from rest_framework.routers import DefaultRouter

from .views import StudentViewSet, TeacherViewSet

router = DefaultRouter()
router.register('student', StudentViewSet)
router.register('teacher', TeacherViewSet)


app_name = 'people'

urlpatterns = [
    path('api/', include(router.urls)),
    #path('api/student', StudentListView.as_view()),
    #path('api/teacher', TeacherListView.as_view()),
    ##path('api/student/<int:pk>', StudentDetailView.as_view()),
]