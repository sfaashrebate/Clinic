from rest_framework.response import Response
from rest_framework import viewsets
from app.models import Reservations, Service, Specification,Doctor
from app.serializers import (
    ServiceSerializer,#

    DetailedSpecificationSerializer,

    DoctorSerializer,#
    DetailedDoctorSerializer,#
    
    ReservationSerializer,#
)
from  django_filters.rest_framework import(
    DjangoFilterBackend,
)
from rest_framework.filters import OrderingFilter,SearchFilter
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
    serializer_class =DetailedSpecificationSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [OrderingFilter,DjangoFilterBackend,]
    filterset_fields =[
        'service_id',
        'name',
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
        'rate',
    ]


class DetailedDoctorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class =DetailedDoctorSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [OrderingFilter,DjangoFilterBackend,]
    filterset_fields =[
        'id',
        'doc_name',
    ]
    
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservations.objects.all()
    serializer_class =ReservationSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [OrderingFilter,DjangoFilterBackend,SearchFilter]
    filterset_fields =[
        'doctor_id',
        'doctor_id__doc_name',
        'doctor_id__spcificaton_id__name',
        'price',
    ]

    def list_patient_reservation(self, request, *args, **kwargs):
        user = self.request.user
        queryset = self.filter_queryset(
            self.get_queryset().filter(paitient_id=user)
        )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
