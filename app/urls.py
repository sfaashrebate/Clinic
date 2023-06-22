from django.urls import path, include
from app.views import (
    ServiceViewSet,
    SpecificationViewSet,
    DoctorViewSet,
    ReservationViewSet,
    DetailedDoctorViewSet,

)
from rest_framework.routers import DefaultRouter

service_router = DefaultRouter()
service_router.register('service', ServiceViewSet, basename='service')

specification_router = DefaultRouter()
specification_router.register('specification', SpecificationViewSet, basename='specification')


doctor_router = DefaultRouter()
doctor_router.register('doctor', DoctorViewSet, basename='doctor')

reservation_router = DefaultRouter()
reservation_router.register('reservation', ReservationViewSet, basename='reservation')
reservation_router.register('doctors-busy-times', DetailedDoctorViewSet, basename='doctors-busy-times')


urlpatterns = [
    path('', include(service_router.urls),name='service' ),
    path('', include(specification_router.urls),name='specification' ),
    path('', include(doctor_router.urls),name='doctor' ),
    path('', include(reservation_router.urls),name='reservation' ),

]