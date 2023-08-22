from asyncore import read, write
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

BMI_DICT = {
    'نحيف جدا':'ننصحك باتباع نظام غذائي لزيادة الوزن',
    'وزن طبيعي':'وزن طبيعي يجب المحافظة عليه',
    'وزن زائد':'ننصحك باتباع نظام غذائي لانقاص الوزن',
    'وزن زائد جدا':'ننصحك باتباع نظام غذائي صارم',
}

def calculate_bmi(weight, height, gender):
    """Calculate BMI based on weight, height and gender"""
    # Convert height to meters
    height = height / 100
    
    # BMI formula
    bmi = weight / (height * height)
    
    # BMI ranges
    if gender == "male":
        if bmi < 18.5:
            return 'نحيف جدا' #BMICategory.UNDERWEIGHT 
        elif 18.5 <= bmi < 25:
            return 'وزن طبيعي' #BMICategory.NORMAL
        elif 25 <= bmi < 30:
            return 'وزن زائد'#BMICategory.OVERWEIGHT
        else:
            return 'وزن زائد جدا'#BMICategory.OBESE
    else:
        if bmi < 18.5:
            return 'نحيف جدا' #BMICategory.UNDERWEIGHT 
        elif 18.5 <= bmi < 24:
            return 'وزن طبيعي' #BMICategory.NORMAL
        elif 24 <= bmi < 29:
            return 'وزن زائد'#BMICategory.OVERWEIGHT
        else:
            return 'وزن زائد جدا'#BMICategory.OBESE


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

    def to_representation(self, instance):
        ret =  super().to_representation(instance)
        bmi_result = ret['bmi_result']
        ret['advice_message']= BMI_DICT[bmi_result]
        return ret
        