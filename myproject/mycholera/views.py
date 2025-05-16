from venv import logger
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
import logging
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View

# Create your views here.


def generic_api(model_class, serializer_class):
    @api_view(['GET', 'POST', 'PUT', 'DELETE'])
    def api_handler(request, pk=None):
        logger.debug(f"Request method: {request.method}, Data: {request.data}")
        
        if request.method == 'GET':
            if pk:
                try:
                    instance = model_class.objects.get(id=pk)
                    serializer = serializer_class(instance)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                instances = model_class.objects.all()
                serializer = serializer_class(instances, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'PUT':
            if pk:
                try:
                    instance = model_class.objects.get(id=pk)
                    serializer = serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
            return Response({'message': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            if pk:
                try:
                    instance = model_class.objects.get(id=pk)
                    instance.delete()
                    return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
            return Response({'message': 'ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Invalid Method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    return api_handler

manage_region = generic_api(Region, RegionSerializer)
manage_district = generic_api(District, DistrictSerializer)
manage_street = generic_api(Street, StreetSerializer)
manage_health_facility = generic_api(HealthFacility, HealthFacilitySerializer)
manage_local_officer = generic_api(LocalOfficer, LocalOfficerSerializer)
manage_doctor = generic_api(Doctor, DoctorSerializer)
manage_patient = generic_api(Patient, PatientSerializer)
manage_health_supervisor = generic_api(HealthSupervisor, HealthSupervisorSerializer)
manage_case_report = generic_api(CaseReport, CaseReportSerializer)