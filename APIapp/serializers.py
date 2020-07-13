from rest_framework import serializers
from .models import OpenlabModel


class OpenlabSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenlabModel
        fields = ('name', 'email')
