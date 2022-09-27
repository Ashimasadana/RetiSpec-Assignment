from .models import Acquisition
from rest_framework import serializers


class AcquisitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Acquisition
        fields = ('Eye', 'Patient', 'SiteName', 'DateTaken', 'OperatorName', 'ImageData')

    def create(self, validated_data):
        acquisition_data = Acquisition.objects.create(**validated_data)
        return acquisition_data
