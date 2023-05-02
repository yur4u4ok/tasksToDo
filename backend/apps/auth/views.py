from rest_framework.generics import CreateAPIView

from apps.users.serializers import UserSerializer
from .serializers import TokenPairSerializer

from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class TokenPairView(TokenObtainPairView):
    serializer_class = TokenPairSerializer


class AuthRegisterView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
