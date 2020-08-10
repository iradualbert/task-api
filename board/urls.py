from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import api

router = DefaultRouter()
router.register('sprints', api.SprintViewSet)
router.register('tasks', api.TaskViewSet)
router.register('users', api.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/auth', obtain_auth_token, name="auth-token"),
] 