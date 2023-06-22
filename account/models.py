from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES =[
    ('male','male'),
    ('female','female'),
]
#Create custom user
class Account(AbstractUser):
    phone                   = models.CharField(max_length=10, default="0912345678", null=True, blank=True)
    notes                   = models.CharField(max_length=255, default="", null=True, blank=True)
    address                 = models.CharField(max_length=255, default="")
    length                 = models.FloatField()
    weight                 = models.FloatField()
    gender                 = models.CharField(max_length=100, default="female",choices=GENDER_CHOICES)
