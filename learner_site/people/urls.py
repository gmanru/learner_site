from django.urls import path, include


from rest_framework.routers import DefaultRouter

from .views import StudentViewSet, TeacherViewSet, UserList, UserDetail, GroupList

router = DefaultRouter()
router.register('student', StudentViewSet)
router.register('teacher', TeacherViewSet)


# app_name = 'people'

urlpatterns = [
    path('api/', include(router.urls)),
    path('o/', include("oauth2_provider.urls", namespace="oauth2_provider")),
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetail.as_view()),
    path('groups/', GroupList.as_view()),
]
