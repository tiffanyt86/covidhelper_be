from django.shortcuts import render
from django.http import Http404
from .models import Patient, Vaccine, VaccineRecord
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from .serializers import VaccineSerializer, PatientSerializer, VaccineRecordSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
# from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token

class HelloWorld(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        return Response("Hello World")

# USER-RELATED VIEWS

@method_decorator(ensure_csrf_cookie, name="dispatch")
class GetCSRFToken(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return Response({ "success": "CSRF cookie set"})

@method_decorator(csrf_protect, name='dispatch')
class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        isAuthenticated = User.is_authenticated

        if isAuthenticated:
            return Response({ "isAuthenticated": "success" })
        
        return Response({ "isAuthenticated": "error" })

# @method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    permission_classes = [AllowAny]

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

# might need to remove this method decorator
# @method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = self.request.data

        username = data["username"]
        password = data["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            auth.login(request, user)
            return Response([token.key, user.pk])
        
        # return Response({ "error": "Error logging in..." })
        return Response(status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request, format=None):
        try: 
            request.user.auth_token.delete()
            return Response("successfully logged out")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# MODEL VIEWS

class VaccineViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = VaccineSerializer
    
    def get_queryset(self):
        vaccines = Vaccine.objects.all()

        return vaccines

class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer
    
    def get_queryset(self):
        patients = Patient.objects.all()

        return patients

class MyPatientsList(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, format=None):
        patients = Patient.objects.filter(provider_id=request.user.id)
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print(request.data)
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VaccineRecordViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VaccineRecordSerializer
    
    def get_queryset(self):
        records = VaccineRecord.objects.all()

        return records
    

    