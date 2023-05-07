from django.contrib import admin
from app.models import Service,Specification,Reservations,Doctor
# Register your models here.
admin.site.register(Service)

admin.site.register(Specification)

admin.site.register(Reservations)
admin.site.register(Doctor)

