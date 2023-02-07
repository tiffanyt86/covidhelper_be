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

class Hello(APIView):
    permission_classes = [IsNotAuthenticated]

    def get(self, request, format=None):
        return Response("Hello World")

# @method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    # permission_classes = (permissions.AllowAny, )
    permission_classes = [IsNotAuthenticated]

    def post(self, request, format=None):
        data = self.request.data

        username = data["username"]
        email = data["email"]
        password = data["password"]
        first_name=data["first_name"]
        last_name=data["last_name"]

        print(username)
        print(email)
        print(password)
        print(first_name)
        print(last_name)

        return Response("Success!")

        # if User.objects.filter(username=username).exists():
        #     return Response({ 'error': 'Sorry, username already taken' })
        # else:
        #     user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        #     user = User.objects.get(id=user.id)


            # return Response({ 'success': 'User {user.username} created' })