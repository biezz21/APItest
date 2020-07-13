from django.shortcuts import render
from rest_framework import viewsets
from .models import OpenlabModel
from .serializers import OpenlabSerializer

# Create your views here.


class OpenlabViewset(viewsets.ModelViewSet):
    serializer_class = OpenlabSerializer
    queryset = OpenlabModel.objects.all()
