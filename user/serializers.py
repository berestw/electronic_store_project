from rest_framework import serializers

from user.models import Users


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя."""
    class Meta:
        model = Users
        fields = ("email", "password",)


class UserListSerializer(serializers.ModelSerializer):
    """Сериализатор списка пользователей."""
    class Meta:
        model = Users
        fields = ("email",)
