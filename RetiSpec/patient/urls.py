from django.urls import path
from .views import CreatePatient, GetPatientByID, GetPatientByName, delete_view

urlpatterns = [
               path('CreatePatient/', CreatePatient.as_view(), name='CreatePatient'),
               path('GetPatientByID/<id>/', GetPatientByID.as_view(), name='GetPatientByID'),
               path('GetPatientByName/', GetPatientByName.as_view(), name='GetPatientByName'),
               path('DeletePatient/<id>/',delete_view,name='DeletePatient'),
]