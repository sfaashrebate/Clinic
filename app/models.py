import datetime
from django.db import models
from account.models import Account
from django.db.models.signals import post_save
from django.dispatch import receiver

class Service(models.Model):
    name = models.CharField(max_length=50 )
    discerption = models.TextField(max_length=255 , default='', null=True, blank=True )
    icon_path = models.ImageField(default=None, null=True, blank=True )


class Specification(models.Model):
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
 
    name = models.CharField(max_length=50 )
    discerption = models.TextField(max_length=255 , default='', null=True, blank=True )
    icon_path = models.ImageField(default=None, null=True, blank=True )


class Doctor(models.Model):
    # user_id=models.OneToOneField(Account,on_delete=models.CASCADE)
    doc_name =models.CharField(max_length=150)
    spcificaton_id = models.ForeignKey(Specification, on_delete=models.CASCADE)
    # rate= models.IntegerField


class Reservations(models.Model):
    description =models.CharField(max_length=150)

    paitient_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateTimeField(default= datetime.datetime.now(),null=True, blank=True )# will be calculated

    price=models.FloatField()

    def save(self, *args, **kwargs):
        # if not self.end_date:
        # self.end_date = self.start_date + datetime.timedelta(minutes=15)
        super().save(*args, **kwargs)


@receiver(post_save, sender=Reservations)
def set_end_date(sender, instance,created, **kwargs):
    # if not instance.end_date:
    if created:
        instance.end_date = instance.start_date + datetime.timedelta(minutes=15)
        instance.save()

#cacluate the day with the
# @proparity day
# {
# day:
# from : 
# to : }
