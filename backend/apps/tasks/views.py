from rest_framework.generics import ListCreateAPIView, GenericAPIView, ListAPIView
from rest_framework import status
from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser

from apps.tasks.filters import TaskFilter
from apps.tasks.models import TasksModel
from apps.tasks.serializers import TaskSerializer


class ListCreateTasksView(ListCreateAPIView):
    filterset_class = TaskFilter

    def get(self, *args, **kwargs):
        tasks = TasksModel.objects.filter(user=self.request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = TaskSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

        return Response(serializer.data)


class UpdateDeleteTaskView(GenericAPIView):

    def get_queryset(self):
        return TasksModel.objects.filter(user=self.request.user)

    def patch(self, *args, **kwargs):
        data = self.request.data
        task = self.get_object()
        serializer = TaskSerializer(task, data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, *args, **kwargs):
        task = self.get_object()
        task.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskIsDone(GenericAPIView):

    def get_queryset(self):
        return TasksModel.objects.filter(user=self.request.user).filter(status=False)

    def patch(self, *args, **kwargs):
        done_task = self.get_object()

        if done_task.status:
            return Response('this task is already done', status.HTTP_400_BAD_REQUEST)

        done_task.status = True
        done_task.save()

        tasks = TasksModel.objects.filter(user=self.request.user).filter(status=False)

        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class TaskIsUndone(GenericAPIView):

    def get_queryset(self):
        return TasksModel.objects.filter(user=self.request.user).filter(status=True)

    def patch(self, *args, **kwargs):
        undone_task = self.get_object()

        if not undone_task.status:
            return Response('this task is already undone', status.HTTP_400_BAD_REQUEST)

        undone_task.status = False
        undone_task.save()

        tasks = TasksModel.objects.filter(user=self.request.user).filter(status=True)

        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class AdminListTasksView(ListAPIView):
    queryset = TasksModel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAdminUser, )
