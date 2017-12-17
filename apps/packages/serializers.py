# Python imports


# Django imports


# Third party apps imports
from rest_framework import serializers


# Local imports
from .models import Activity, Package


# Create your serializers here.
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ("name", "description", "hours", "days", "image",)


class PackageSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = Package
        fields = (
            "id", "name", "description", "price", "duration", "image",
            "activities",)
