from django.contrib import admin
from app.models import Service, Specification, Reservations, Doctor
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'discerption', 'icon_path')


class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_id', 'name', 'discerption', 'icon_path')


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'doc_name', 'spcificaton_id', 'rate', 'price')

class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'paitient_id',
                    'doctor_id', 'start_date', 'end_date', 'price')
admin.site.register(Service, ServiceAdmin)
admin.site.register(Specification, SpecificationAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Reservations, ReservationsAdmin)
