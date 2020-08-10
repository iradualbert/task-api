from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Sprint, Task

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="get_full_name", read_only=True)

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active')


class SprintSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    
    class Meta:
        model = Sprint
        fields = ('id', 'name', 'description', 'end', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('sprint-detail',
            kwargs={'pk': obj.pk}, request=request
            )
        }

class TaskSerializer(serializers.ModelSerializer):
    assigned = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, required=False, read_only=True)
    status_display = serializers.SerializerMethodField('get_status_display')
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'sprint', 'status', 'order', 'assigned', 'status_display',
                  'started', 'due', 'completed')

    def get_status_display(self, obj):
        return obj.get_status_display()
