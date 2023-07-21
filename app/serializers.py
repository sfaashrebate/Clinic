
from asyncore import read
from rest_framework import serializers
from app.models import Doctor, Reservations, Service, Specification

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id','name','discerption','icon_path',#'__all__'
        ]


class DetailedSpecificationSerializer(serializers.ModelSerializer):
    service_details = ServiceSerializer(source='service_id',read_only=True)

    class Meta:
        model = Specification
        fields = [
            'id',
            'name',
            'discerption',
            'icon_path',
            'service_id',
            'service_details',
        ]

class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = [
            'id','name','discerption','icon_path','service_id'
        ]

# do reservation serializer ***************
# .....
class ReservationSerializer(serializers.ModelSerializer):
    from_date = serializers.DateTimeField(source='start_date', format="%H:%M %d-%m-%Y")
    to_date = serializers.DateTimeField(
        source='end_date',
        format="%H:%M %d-%m-%Y",
        read_only=True,
    )
    paitient_id = serializers.PrimaryKeyRelatedField(read_only =True)

    class Meta:
        model = Reservations
        fields =[
            'id',
            'description',
            'paitient_id',
            'doctor_id',
            'from_date',
            'to_date',
            'price',
        ]

    def create(self, validated_data):
        patient = self.context['request'].user
        validated_data['paitient_id'] = patient
        return super().create(validated_data)

class DoctorSerializer(serializers.ModelSerializer):
    spcificaton_details = SpecificationSerializer(read_only=True,source='spcificaton_id')

    class Meta:
        model = Doctor
        fields = (
            'id',
            'doc_name',
            'spcificaton_id',
            'spcificaton_details',
        )

class DoctorBusyTimeSerializer(serializers.ModelSerializer):
    from_date = serializers.DateTimeField(source='start_date', format="%H:%M %d-%m-%Y")
    to_date = serializers.DateTimeField(source='end_date', format="%H:%M %d-%m-%Y")
    # user = serializers.CharField(source='paitient_id.username')

    class Meta:
        model = Reservations
        fields = (
            'id',
            'from_date',
            'to_date'
        )
        #, 'user')

class DetailedDoctorSerializer(serializers.ModelSerializer):
    busy_time = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Doctor
        fields = (
            'id',
            'doc_name',
            'busy_time',
        )
    
    # Serializer method field
    def get_busy_time(self, obj): # object = doctor
        reservations = Reservations.objects.filter(doctor_id=obj)
        serializer = DoctorBusyTimeSerializer(reservations, many=True)
        print(serializer.data)
        return serializer.data # dict


class MyReservationSerializer(serializers.ModelSerializer):
    from_date = serializers.DateTimeField(
        source='start_date',
        format="%H:%M %d-%m-%Y",
        read_only=True,
    )
    to_date = serializers.DateTimeField(
        source='end_date',
        format="%H:%M %d-%m-%Y",
        read_only=True,
    )
    current_user= serializers.CurrentUserDefault()
    paitient_id = serializers.PrimaryKeyRelatedField(
            read_only= True
    )
    class Meta:
        model = Reservations
        fields =[
            'id',
            'description',
            'paitient_id',
            'doctor_id',
            'from_date',
            'to_date',
            'price',
        ]

    def to_representation(self, instance):
        print(instance)
        # patient = 
        # print(patient)
        return super().to_representation(instance)
