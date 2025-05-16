from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from mycholera.views import *
from mycholera.views import api_view

urlpatterns = [
    path('region/', manage_region),
    path('region/<int:id>/', manage_region),

    path('district/', manage_district),
    path('district/<int:id>/', manage_district),

    path('street/', manage_street),
    path('street/<int:id>/', manage_street),

    path('health-facility/', manage_health_facility),
    path('health-facility/<int:id>/', manage_health_facility),

    path('local-officer/', manage_local_officer),
    path('local-officer/<int:id>/', manage_local_officer),

    path('doctor/', manage_doctor),
    path('doctor/<int:id>/', manage_doctor),

    path('patient/', manage_patient),
    path('patient/<int:id>/', manage_patient),

    path('health-supervisor/', manage_health_supervisor),
    path('health-supervisor/<int:id>/', manage_health_supervisor),

    path('case-report/', manage_case_report),
    path('case-report/<int:id>/', manage_case_report),

    # path('login/', LoginView.as_view(), name='login'),
]
