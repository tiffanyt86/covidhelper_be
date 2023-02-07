from django.shortcuts import render
from .models import Patient, Vaccine
from django.contrib.auth.models import User
from django.contrib import auth
from .serializers import UserSerializer, VaccineSerializer, PatientSerializer
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsNotAuthenticated

# MODEL VIEWS

# class VaccineViewSet(viewsets.ModelViewSet):
#     serializer_class = VaccineSerializer
#     queryset = Vaccine.objects.all()

class HelloWorld(APIView):
    permission_classes = [IsNotAuthenticated]

    def get(self, request, format=None):
        return Response("Hello World")
    