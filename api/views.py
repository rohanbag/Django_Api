from django.shortcuts import render
from rest_framework import viewsets
from .models import Matl
from .serializer import MatlSerializer

class MatlView(viewsets.ModelViewSet):
	queryset = Matl.objects.all()
	serializer_class = MatlSerializer