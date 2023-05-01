from django.urls import path

from .views import ListCreateTasksView, UpdateDeleteTaskView, TaskIsDone, TaskIsUndone, AdminListTasksView

urlpatterns = [
    path('', ListCreateTasksView.as_view(), name='tasks'),
    path('/<int:pk>', UpdateDeleteTaskView.as_view(), name='update_delete_task'),
    path('/<int:pk>/done', TaskIsDone.as_view(), name='done_task'),
    path('/<int:pk>/undone', TaskIsUndone.as_view(), name='undone_task'),
    path('/all', AdminListTasksView.as_view(), name='all_tasks')
]
