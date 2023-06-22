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
service_router.register('', ServiceViewSet, basename='service')

specification_router = DefaultRouter()
specification_router.register('', SpecificationViewSet, basename='specification')


doctor_router = DefaultRouter()
doctor_router.register('', DoctorViewSet, basename='doctor')

reservation_router = DefaultRouter()
reservation_router.register('', ReservationViewSet, basename='reservation')
reservation_router.register('doctors-busy-times', DetailedDoctorViewSet, basename='doctors-busy-times')


urlpatterns = [
    path('service/', include(service_router.urls),name='service' ),
    path('specification/', include(specification_router.urls),name='specification' ),
    path('doctor/', include(doctor_router.urls),name='doctor' ),
    path('reservation/', include(reservation_router.urls),name='reservation' ),

]