from django.db import models
from django.contrib.auth import get_user_model
from apps.users.models import ProfileModel, UserModel as User

UserModel: User = get_user_model()


class TasksModel(models.Model):
    class Meta:
        db_table = 'tasks'

    task = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='tasks')
