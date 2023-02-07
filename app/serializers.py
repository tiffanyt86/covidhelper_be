from .models import Patient, Vaccine
from django.contrib.auth.models import User
from rest_framework import serializers

# SERIALIZERS to convert from dict to JSON

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = "__all__"

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
