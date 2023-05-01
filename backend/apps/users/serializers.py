from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from apps.users.models import ProfileModel, UserModel as User
from django.db import transaction

UserModel: User = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age')


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser',
                  'created_at', 'updated_at', 'profile')
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser',
                            'created_at', 'updated_at')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @transaction.atomic
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user
