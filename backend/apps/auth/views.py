from rest_framework.generics import CreateAPIView

from apps.users.serializers import UserSerializer
from rest_framework.permissions import AllowAny


class AuthRegisterView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
