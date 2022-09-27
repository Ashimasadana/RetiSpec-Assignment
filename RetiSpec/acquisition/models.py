from django.db import models
from django.utils import timezone
from patient.models import Patient

# Create your models here.

class Acquisition(models.Model):
    AcquisitionID = models.AutoField(primary_key=True)
    EYE_CHOICES = (
        ('L', 'Left',),
        ('R', 'Right',),
    )
    Eye = models.CharField(max_length=1, choices=EYE_CHOICES, null=True)
    Patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    SiteName = models.CharField(max_length=50, blank=True, null=True)
    DateTaken = models.DateField()
    OperatorName = models.CharField(max_length=50, blank=True, null=True)
    ImageData = models.ImageField(upload_to='ImageData',blank=True,null=True)
