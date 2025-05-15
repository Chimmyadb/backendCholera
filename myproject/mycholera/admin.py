from django.contrib import admin
from .models import*

admin.site.register(Region)
admin.site.register(District)
admin.site.register(Street)
admin.site.register(HealthFacility)
admin.site.register(LocalOfficer)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(HealthSupervisor)
admin.site.register(CaseReport)

