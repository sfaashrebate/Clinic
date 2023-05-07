from django.conf import settings
from rest_framework import serializers
from account.models import Account
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
            'phone',
            'notes',
            'address',
            'types',
            ]
            
        extra_kwargs = {
        'password': {'write_only': True},
    }

    def create(self, validated_data):

        password = validated_data['password']
        instance =Account(**validated_data)
        instance.set_password(password) # for encode the password
        obj = instance.save()
        return instance
