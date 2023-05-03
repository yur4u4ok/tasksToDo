from rest_framework.generics import GenericAPIView, ListAPIView

from apps.users.serializers import UserSerializer
from core.permissions.is_superuser import IsSuperUser
from rest_framework.permissions import IsAdminUser

from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
from apps.users.models import UserModel as User

UserModel: User = get_user_model()


# FOR SUPERUSER
class UserToAdmin(GenericAPIView):
    permission_classes = (IsSuperUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_staff:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user.is_staff = True
        user.save()
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)


# FOR SUPERUSER
class AdminToUser(GenericAPIView):
    permission_classes = (IsSuperUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_staff:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user.is_staff = False
        user.save()
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)


# FOR ADMIN
class AllUsersView(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.id)
