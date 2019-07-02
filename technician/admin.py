from django.contrib import admin

from technician.models import Technician, Company, Service, TechnicianToService

admin.site.register(Technician)
admin.site.register(Company)
admin.site.register(Service)
admin.site.register(TechnicianToService)
