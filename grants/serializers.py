from rest_framework import serializers
from .models import Grant, ScienceDirection, Result


class GrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grant
        fields = '__all__'


class ScienceDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScienceDirection
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
