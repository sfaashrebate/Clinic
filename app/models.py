import datetime
from django.db import models
from account.models import Account


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
    user_id=models.OneToOneField(Account,on_delete=models.CASCADE)
    spcificaton_id = models.ForeignKey(Specification, on_delete=models.CASCADE)


class reserrations(models.Model):
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateTimeField(default= datetime.timedelta(seconds=10),null=True, blank=True )# will be calculated
    description =models.CharField(max_length=150)
    price=models.FloatField()
    rate= models.IntegerField

    paitient_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Doctor, on_delete=models.CASCADE) 

#cacluate the day with the
# @proparity day
# {
# day:
# from : 
# to : }

         



 

