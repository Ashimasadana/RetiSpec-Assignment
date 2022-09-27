from django.urls import path
from .views import AddAcquisition, ListAcquistionsOfPatient, delete_view, DownloadAcquistionImage

urlpatterns = [
               path('AddAcquisition/', AddAcquisition.as_view(), name='AddAcquisition'),
               path('ListAcquistionsOfPatient/<id>/', ListAcquistionsOfPatient.as_view(), name='ListAcquistionsOfPatient'),
               path('DeleteAcquisition/<id>/',delete_view,name='DeleteAcquisition'),
               path('DownloadAcquistionImage/<id>/', DownloadAcquistionImage, name='DownloadAcquistionImage'),
]