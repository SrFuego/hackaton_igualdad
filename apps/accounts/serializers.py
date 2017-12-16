# Python imports


# Django imports
from django.contrib.auth import get_user_model


# Third party apps imports
from rest_framework import serializers
from rest_framework.utils import model_meta


# Local imports
from .models import Account


# Create your serializers here.
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "password", "first_name", "last_name", "email",)


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ("id", "user", "cell_phone", "dni", "ubigeo",)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            validated_data["user"]["username"],
            validated_data["user"]["email"],
            validated_data["user"]["password"],
            first_name=validated_data["user"]["first_name"],
            last_name=validated_data["user"]["last_name"])
        validated_data.pop("user")
        info = model_meta.get_field_info(Account)
        many_to_many = {}
        for field_name, relation_info in info.relations.items():
            if relation_info.to_many and (field_name in validated_data):
                many_to_many[field_name] = validated_data.pop(field_name)
        instance = Account.objects.create(user=user, **validated_data)
        if many_to_many:
            for field_name, value in many_to_many.items():
                field = getattr(instance, field_name)
                field.set(value)
        return instance
