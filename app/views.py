from django.shortcuts import render
from .models import Patient, Vaccine
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from .serializers import UserSerializer, VaccineSerializer, PatientSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
# from .permissions import IsNotAuthenticated

# MODEL VIEWS

# class VaccineViewSet(viewsets.ModelViewSet):
#     serializer_class = VaccineSerializer
#     queryset = Vaccine.objects.all()

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

@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = self.request.data

        username = data["username"]
        password = data["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return Response({ "Success": "User authenticated", "username": username })
        
        return Response({ "error": "Error authenticating" })

class LogoutView(APIView):
    def post(self, request, format=None):
        try: 
            auth.logout(request)
            return Response({ "success": "Logged Out" })
        except:
            return Response({ "error": "Something went wrong when logging out" })