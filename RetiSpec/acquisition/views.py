from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from rest_framework.response import Response
from .serializers import AcquisitionSerializer
from .models import Acquisition
from rest_framework import generics
import json
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework.views import APIView

# Create your views here.

#Add a new acquisition for a patient
class AddAcquisition(generics.GenericAPIView):
    serializer_class = AcquisitionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        acquisition_data = serializer.save()
        try:
            acquisition_data_query=Acquisition.objects.filter(AcquisitionID=acquisition_data.AcquisitionID).values()[0]
            return Response({
                'patient_data': acquisition_data_query,
                'msg': 'Acquisition created Successfully',
                'status': 200
            })
        except Exception as esc:
            print(esc)

#List all patient acquisitions (by patient id)
class ListAcquistionsOfPatient(generics.ListAPIView):
    def get(self, request, id, *args, **kwargs):
        try:
            return Response(Acquisition.objects.filter(Patient_id=id).values('AcquisitionID', 'Eye', 'Patient_id', 'SiteName', 'DateTaken', 'OperatorName'))            
        except Exception as esc:
            print(esc)
            return Response({'Exception':esc})            

#Delete Acquisition
def delete_view(request, id):
    context ={}
    obj = get_object_or_404(Acquisition, AcquisitionID = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "delete_acquisition.html", context)            

#Download an image (by acquisition id)
def DownloadAcquistionImage(request, id):
    context ={}
    obj = get_object_or_404(Acquisition, AcquisitionID = id)
    context['download_url'] = obj.ImageData.url
    
    # if request.method == 'POST':
    #     download_url = obj.ImageData.url
    #     print(download_url)
    #     return HttpResponseRedirect(download_url)
    return render(request, "download_acquisition_image.html", context)  