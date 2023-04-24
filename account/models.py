from email.mime import image
from operator import truediv
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from datetime import  datetime, timedelta,date
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from django.dispatch import receiver
from django.forms import DateField
from rest_framework.authtoken.models import Token

from app.models import Specification

TYPES = (
    ('Doctor','Doctor'),
    ('Admin','Admin'),
	('patient','patient'),
)

class Account(AbstractUser):
    phone                   = models.CharField(max_length=10, default="0912345678", null=True, blank=True)
    notes                   = models.CharField(max_length=255, default="", null=True, blank=True)
    address                   = models.CharField(max_length=255, default="")
	
    types                   = models.CharField(max_length=10, default="", choices=TYPES)


class Doctor(model.Models):
    user_id=models.OneToOneField(Account,on_delete=models.CASCADE)
    spcificaton_id = models.ForeignKey(Specification, on_delete=models.CASCADE)
