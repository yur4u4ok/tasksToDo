from rest_framework.serializers import ModelSerializer, RelatedField

from apps.tasks.models import TasksModel
from core.dataclasses.user_dataclasses import User


class UserTaskSerializer(RelatedField):
    def to_representation(self, value: User):
        return {"id": value.id, "email": value.email}


class TaskSerializer(ModelSerializer):
    user = UserTaskSerializer(read_only=True)

    class Meta:
        model = TasksModel
        fields = ('id', 'task', 'status', 'created_at', 'updated_at', 'user')
        read_only_fields = ('user',)
