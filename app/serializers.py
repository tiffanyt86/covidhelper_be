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
    provider_id = serializers.ReadOnlyField(source='request.user.id')
    # provider_id = serializers.ReadOnlyField(source='request.user.id')
    class Meta:
        model = Patient
        fields = '__all__'
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Patient.objects.create(**validated_data)
