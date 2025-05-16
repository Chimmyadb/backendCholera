from rest_framework import serializers
from .models import *

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
       

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'
        
        
class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'
       
        
class HealthFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthFacility
        fields = '__all__'
       

class LocalOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalOfficer
        fields = '__all__'
        

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        
class HealthSupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthSupervisor
        fields = '__all__'
        
        
class CaseReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseReport
        fields = '__all__'
       