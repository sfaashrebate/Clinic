from asyncore import write
from enum import Enum
from random import choices
from django.conf import settings
from rest_framework import serializers
from account.models import GENDER_CHOICES
from django.contrib.auth import get_user_model

User = get_user_model()

from enum import Enum

class BMICategory(Enum):
    UNDERWEIGHT =  "Underweight"
    NORMAL = "Normal weight" 
    OVERWEIGHT = "Overweight"
    OBESE = "Obese"


def calculate_bmi(weight, height, gender):
    """Calculate BMI based on weight, height and gender"""
    # Convert height to meters
    height = height / 100
    
    # BMI formula
    bmi = weight / (height * height)
    
    # BMI ranges
    if gender == "male":
        if bmi < 18.5:
            return 'Underweight' #BMICategory.UNDERWEIGHT 
        elif 18.5 <= bmi < 25:
            return 'Normal weight' #BMICategory.NORMAL
        elif 25 <= bmi < 30:
            return 'Overweight'#BMICategory.OVERWEIGHT
        else:
            return 'Obese'#BMICategory.OBESE
    else:
        if bmi < 18.5:
            return 'Underweight' #BMICategory.UNDERWEIGHT 
        elif 18.5 <= bmi < 24:
            return 'Normal weight' #BMICategory.NORMAL
        elif 24 <= bmi < 29:
            return 'Overweight'#BMICategory.OVERWEIGHT
        else:
            return 'Obese'#BMICategory.OBESE


class BMISerializer(serializers.Serializer):
    weight = serializers.FloatField(write_only=True)
    height = serializers.FloatField(write_only=True)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES,write_only=True)
    bmi_result = serializers.SerializerMethodField(read_only =True)

    class Meta:
        fields = [
            'weight',
            'height',
            'gender',
            'bmi_result',
            ]

    def get_bmi_result(self,obj):
        bmi_result =calculate_bmi(
            obj['weight'],
            obj['height'],
            obj['gender'],
        )
        return bmi_result
