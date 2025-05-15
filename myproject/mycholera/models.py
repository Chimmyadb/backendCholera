from django.db import models
# from django.contrib.auth.models import 

class Region(models.Model):
    regionId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    
class District(models.Model):
    district=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    population=models.IntegerField()
    region=models.ForeignKey(Region, on_delete=models.CASCADE)

class Street(models.Model):
    streetId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    totalPopulation=models.IntegerField()
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    
class HealthFacility(models.Model):
    facilityId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    street=models.ForeignKey(Street, on_delete=models.CASCADE)
    
class LocalOfficer(models.Model):
    officerId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    street=models.ForeignKey(Street, on_delete=models.CASCADE)
    
class Doctor(models.Model):
    doctorId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    specialization=models.CharField(max_length=100)
    facility=models.ForeignKey(HealthFacility, on_delete=models.CASCADE)
    
class Patient(models.Model):
    patientId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    age=models.IntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address=models.TextField()
    condition=models.TextField()
    status=models.CharField(max_length=50)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    street=models.ForeignKey(Street, on_delete=models.CASCADE)
    officer=models.ForeignKey(LocalOfficer, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.phone} - {self.age} - {self.address}- {self.gender} - {self.condition} - {self.status} - {self.doctor} - {self.street} - {self.officer}"

    
class HealthSupervisor(models.Model):
    supervisorId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    
class CaseReport(models.Model):
    reportId=models.AutoField(primary_key=True)
    reportDate=models.DateField()
    status=models.CharField(max_length=50)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    supervisor=models.ForeignKey(HealthSupervisor, on_delete=models.CASCADE)


