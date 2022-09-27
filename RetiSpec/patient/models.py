from django.db import models
from django.utils import timezone

# Create your models here.

class Patient(models.Model):
    PatientID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50, blank=True, null=True)
    LastName = models.CharField(max_length=50, blank=True, null=True)
    DateOfBirth = models.DateField()
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('U', 'Unsure',),
    )
    Sex = models.CharField(max_length=1, default='U', choices=SEX_CHOICES)
