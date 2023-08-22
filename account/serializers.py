from rest_framework import serializers
from account.models import GENDER_CHOICES, Account
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

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
            'gender',
            'profile_pic',
        ]

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        print(validated_data)
        password = validated_data['password']
        instance = User(**validated_data)
        instance.set_password(password)  # for encode the password
        instance.save()
        print(instance.password)
        print(check_password(password ,instance.password))
        return instance

    def update(self, instance, validated_data):
        password = validated_data.get('password',None)
        if password:
            password = validated_data.pop('password')
        instance = super().update(instance, validated_data)
        return instance



class PasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(source= "password",write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'old_password',
            'new_password',
        ]

    def update(self, instance, validated_data):
        print(validated_data)
        old_password = validated_data.pop('password')
        new_password = validated_data.pop('new_password')
        print('pass before reset', instance.password)
        print(old_password)
        print(check_password(old_password ,instance.password))
        if check_password(old_password ,instance.password):
            print('sssss')
            instance.set_password(new_password)  # for encode the password
            print('pass after reset' ,instance.password)
        else:
            raise serializers.ValidationError('please enter your correct password')

        instance = super().update(instance, validated_data)
        return instance

    def to_representation(self, instance):

        return {'response':'success'}