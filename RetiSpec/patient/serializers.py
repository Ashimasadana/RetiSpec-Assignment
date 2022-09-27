from .models import Patient
from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ('FirstName', 'LastName', 'DateOfBirth', 'Sex')

    def create(self, validated_data):
        patient_data = Patient.objects.create(**validated_data)
        return patient_data
