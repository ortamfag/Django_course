from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

from user.views import AuthenticationViewSet
from api.views import GroupViewSet, OneViewSet, StudentViewSet, ProjectViewSet

router = DefaultRouter()
router.register('user', AuthenticationViewSet)
router.register('student', StudentViewSet)
router.register('group', GroupViewSet)
router.register('project', ProjectViewSet)
router.register('321', OneViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
