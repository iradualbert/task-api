from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, authentication
from .models import Sprint, Task
from .serializers import SprintSerializer, UserSerializer, TaskSerializer

User = get_user_model()

class DefaultsMixin(object):
    "default settings fro view authentication"
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

class SprintViewSet(DefaultsMixin, viewsets.ModelViewSet):
    "endpoint for listing and creating sprints"
    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer


class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    "endpoint for listing and creating sprints"
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):

    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.all()
    serializer_class = UserSerializer
