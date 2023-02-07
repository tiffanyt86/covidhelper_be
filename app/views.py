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

# @method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    permission_classes = [IsNotAuthenticated]

    def post(self, request, format=None):
        data = self.request.data

        username = data["username"]
        email = data["email"]
        password = data["password"]
        first_name=data["first_name"]
        last_name=data["last_name"]

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            print(user.id)
            return Response({ 'error': 'Sorry, username already taken' })
        
        # create a user object
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

        # fetch the user from the database
        user = User.objects.get(id=user.id)
        return Response('success: User ' + user.username + ' created')