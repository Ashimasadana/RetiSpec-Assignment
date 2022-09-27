from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from rest_framework.response import Response
from .serializers import PatientSerializer
from .models import Patient
from rest_framework import generics
import json
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

# Create your views here.

# Create Patient
class CreatePatient(generics.GenericAPIView):
    serializer_class = PatientSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        patient_data = serializer.save()
        try:
            patient_data_query=Patient.objects.filter(PatientID=patient_data.PatientID).values()[0]
            return Response({
                'patient_data': patient_data_query,
                'msg': 'Patient created Successfully',
                'status': 200
            })
        except Exception as esc:
            print(esc)

# Get a patient by ID
class GetPatientByID(generics.ListAPIView):
    def get(self, request, id, *args, **kwargs):
        try:
            return Response(Patient.objects.filter(PatientID=id).values()[0])            
        except Exception as esc:
            print(esc)
            return Response({'Exception':esc})            

# Get a patient by first + last name
class GetPatientByName(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        try:
            return Response(Patient.objects.filter(Q(FirstName = request.GET['FirstName']) | Q(LastName = request.GET['LastName'])).values())            
        except Exception as esc:
            print(esc)
            return Response({'Exception':esc})            

# Delete Patient
def delete_view(request, id):
    context ={}
    obj = get_object_or_404(Patient, PatientID = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "delete_patient.html", context)            
