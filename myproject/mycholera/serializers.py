from rest_framework import serializers
from .models import *
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
        # fields = ['regionId', 'name']
        # exclude = ['regionId']
        # read_only_fields = ['regionId']
        # extra_kwargs = {'regionId': {'read_only': True}}

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'
        # fields = ['district', 'name', 'population', 'region']
        # exclude = ['district']
        # read_only_fields = ['district']
        # extra_kwargs = {'district': {'read_only': True}}
        
class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'
        # fields = ['streetId', 'name', 'location', 'totalPopulation', 'district']
        # exclude = ['streetId']
        # read_only_fields = ['streetId']
        # extra_kwargs = {'streetId': {'read_only': True}}
        
class HealthFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthFacility
        fields = '__all__'
        # fields = ['facilityId', 'name', 'location', 'phone', 'street']
        # exclude = ['facilityId']
        # read_only_fields = ['facilityId']
        # extra_kwargs = {'facilityId': {'read_only': True}}

class LocalOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalOfficer
        fields = '__all__'
        # fields = ['officerId', 'name', 'phone', 'street']
        # exclude = ['officerId']
        # read_only_fields = ['officerId']
        # extra_kwargs = {'officerId': {'read_only': True}}

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        # fields = ['doctorId', 'name', 'phone', 'specialization', 'facility']
        # exclude = ['doctorId']
        # read_only_fields = ['doctorId']
        # extra_kwargs = {'doctorId': {'read_only': True}}
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        # fields = ['patientId', 'name', 'phone', 'age', '
        
class HealthSupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthSupervisor
        fields = '__all__'
        # fields = ['supervisorId', 'name', 'phone', 'specialization', 'facility']
        # exclude = ['supervisorId']
        # read_only_fields = ['supervisorId']
        # extra_kwargs = {'supervisorId': {'read_only': True}}
        
class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseReport
        fields = '__all__'
        # fields = ['caseId', 'patient', 'healthFacility', 'dateReported', 'status']
        # exclude = ['caseId']
        # read_only_fields = ['caseId']
        # extra_kwargs = {'caseId': {'read_only': True}}