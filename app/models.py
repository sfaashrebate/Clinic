import datetime
from django.db import models
from account.models import Account
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver

from filesmanager.models import Media


class Service(models.Model):
    name = models.CharField(max_length=50)
    discerption = models.TextField(
        max_length=255, default='', null=True, blank=True)
    icon_path =  models.OneToOneField(
        Media, on_delete=models.CASCADE, default=None, null=True,blank=True)

    def __str__(self) -> str:
        return self.name


class Specification(models.Model):
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    discerption = models.TextField(
        max_length=255, default='', null=True, blank=True)
    icon_path =  models.OneToOneField(
        Media, on_delete=models.CASCADE, default=None, null=True,blank=True)


    def __str__(self) -> str:
        return self.name


class Doctor(models.Model):
    doc_name = models.CharField(max_length=150)
    spcificaton_id = models.ForeignKey(Specification, on_delete=models.CASCADE)
    rate = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    price = models.IntegerField()
    profile_pic = models.OneToOneField(
        Media, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self) -> str:
        return self.doc_name


class Reservations(models.Model):
    description = models.CharField(max_length=150)

    paitient_id = models.ForeignKey(
        Account, on_delete=models.CASCADE)  # Account
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True)  # will be calculated


# pre_save signal using decorator
@receiver(pre_save, sender=Reservations)
def reservation_pre_save(sender, instance, **kwargs):
    instance.end_date = instance.start_date + datetime.timedelta(minutes=30)
