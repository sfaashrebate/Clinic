from rest_framework import viewsets
from app.models import Service, Specification,Doctor
from app.serializers import ServiceSerializer, SpecificationSerializer,DoctorSerializer
from  django_filters.rest_framework import(
    DjangoFilterBackend,
)
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter,DjangoFilterBackend,]
    filterset_fields =[
        'name',
    ]

class SpecificationViewSet(viewsets.ModelViewSet):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [OrderingFilter,DjangoFilterBackend,]
    filterset_fields =[
        'name',
        'service_id',
        'service_id__name',
    ]


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [OrderingFilter,DjangoFilterBackend,]
    filterset_fields =[
        'doc_name',
        'spcificaton_id',
        'spcificaton_id__name',
    ]
