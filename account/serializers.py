from rest_framework import serializers
from account.models import GENDER_CHOICES, Account
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountSerializer(serializers.ModelSerializer):
    weight = serializers.FloatField(default=0.00)
    length = serializers.FloatField(default=0.00)

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'password',
            'phone',
            'notes',
            'address',
            'weight',
            'length',
            'gender'
        ]

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data['password']
        instance = User(**validated_data)
        instance.set_password(password)  # for encode the password
        instance.save()
        return instance
