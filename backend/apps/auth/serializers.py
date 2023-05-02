from apps.users.serializers import UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = UserSerializer(self.user).data
        return data
