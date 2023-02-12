from .models import Patient, Vaccine, VaccineRecord
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
        return Patient.objects.create(**validated_data)

class VaccineRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccineRecord
        fields = "__all__"
