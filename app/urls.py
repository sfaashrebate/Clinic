from django.urls import path, include
from app.views import (
    MyReservationViewSet,
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

doctors_busy_times = DefaultRouter()
doctors_busy_times.register('', DetailedDoctorViewSet, basename='doctors-busy-times')

myreservation_router = DefaultRouter()
myreservation_router.register('', MyReservationViewSet, basename='myreservation')

urlpatterns = [
    path('service/', include(service_router.urls),name='service' ),
    path('specification/', include(specification_router.urls),name='specification' ),
    path('doctor/', include(doctor_router.urls),name='doctor' ),
    path('reservation/', include(reservation_router.urls),name='reservation' ),
    path('reservation/myreservation',MyReservationViewSet.as_view(),name='myreservation' ),
    path('doctors-busy-times/', include(doctors_busy_times.urls),name='reservation' ),

]