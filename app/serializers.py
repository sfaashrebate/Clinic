
from rest_framework import serializers
from app.models import Doctor, Reservations, Service, Specification

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id','name','discerption','icon_path',#'__all__'
        ]


class SpecificationSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(source='service_id',read_only=True)

    class Meta:
        model = Specification
        fields = [
            'id','name','discerption','icon_path','service'
        ]

class SpecificationSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = [
            'id','name','discerption','icon_path','service_id'
        ]

class DoctorBusyTimeSerializer(serializers.ModelSerializer):
    from_date = serializers.DateTimeField(source='start_date', format="%H:%M %d-%m-%Y")
    to_date = serializers.DateTimeField(source='end_date', format="%H:%M %d-%m-%Y")
    user = serializers.CharField(source='paitient_id.username')

    class Meta:
        model = Reservations
        fields = ('from_date', 'to_date', 'user')


class DoctorSerializer(serializers.ModelSerializer):
    busy_time = serializers.SerializerMethodField(read_only=True)
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        # read_only=True,
    )
    spcificaton_id = SpecificationSerializer2(read_only=True)

    class Meta:
        model = Doctor
        fields = (
            'id',
            'doc_name',
            'spcificaton_id',

            'user',
            'busy_time',
        )

    def get_busy_time(self, obj):
        reservations = Reservations.objects.filter(doctor_id=obj)
        serializer = DoctorBusyTimeSerializer(reservations, many=True)
        print(serializer.data)
        return serializer.data
