from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from app.models import Reservations, Service, Specification, Doctor
from app.serializers import (
    MyReservationSerializer,
    ServiceSerializer,

    DetailedSpecificationSerializer,

    DoctorSerializer,
    DetailedDoctorSerializer,

    ReservationSerializer,
)
from django_filters.rest_framework import (
    DjangoFilterBackend,
)
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

import django_filters


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter, DjangoFilterBackend,]
    filterset_fields = [
        'name',
    ]


class SpecificationViewSet(viewsets.ModelViewSet):
    queryset = Specification.objects.all()
    serializer_class = DetailedSpecificationSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [OrderingFilter, DjangoFilterBackend,]
    filterset_fields = [
        'service_id',
        'name',
    ]


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [OrderingFilter, DjangoFilterBackend,]
    filterset_fields = [
        'doc_name',
        'spcificaton_id',
        'spcificaton_id__name',
        'rate',
    ]


class DetailedDoctorViewSet(
    GenericViewSet
):
    queryset = Doctor.objects.all()
    serializer_class = DetailedDoctorSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    filter_backends = [OrderingFilter, DjangoFilterBackend,]
    filterset_fields = [
        'id',
        'doc_name',
    ]

    @action(url_path='retrieve', detail=True)
    def get_doctors_busy_times(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(url_path='list', detail=False)
    def list_doctors_busy_times(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ReservationFilter(django_filters.FilterSet):
    price_lte = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte')  # less than or equal
    price_gte = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte')  # greater than or equal

    class Meta:
        model = Reservations
        fields = ['price_lte', 'price_gte']


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservations.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = ReservationFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend, SearchFilter]
    filterset_fields = [
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


class MyReservationViewSet(
        GenericViewSet):

    queryset = Reservations.objects.all()
    serializer_class = MyReservationSerializer
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        queryset = self.get_queryset().filter(paitient_id=self.request.user)
        return super().filter_queryset(queryset)

    @action(url_path='', url_name='myreservation', detail=False)
    def myreservation(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
