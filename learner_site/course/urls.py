from django.urls import path, include


from rest_framework.routers import DefaultRouter

from .views.cb_views import CourseViewSet

router = DefaultRouter()
router.register('', CourseViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
