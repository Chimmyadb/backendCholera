from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from mycholera.views import *
from mycholera.views import api_view

urlpatterns = [
    path('regions/', manage_region),
    path('region/<int:pk>/', manage_region),

    path('districts/', manage_district),
    path('district/<int:pk>/', manage_district),

    path('streets/', manage_street),
    path('street/<int:pk>/', manage_street),

    path('health-facility/', manage_health_facility),
    path('health-facility/<int:pk>/', manage_health_facility),

    path('local-officers/', manage_local_officer),
    path('local-officer/<int:pk>/', manage_local_officer),

    path('doctors/', manage_doctor),
    path('doctor/<int:pk>/', manage_doctor),

    path('patients/', manage_patient),
    path('patient/<int:pk>/', manage_patient),

    path('health-supervisors/', manage_health_supervisor),
    path('health-supervisor/<int:pk>/', manage_health_supervisor),

    path('case-reports/', manage_case_report),
    path('case-report/<int:pk>/', manage_case_report),

    # path('login/', LoginView.as_view(), name='login'),
]
