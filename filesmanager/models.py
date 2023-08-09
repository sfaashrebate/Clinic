from django.db import models

# Create your models here.

class Media(models.Model):
    file = models.FileField()

class TestModel(models.Model):
    name = models.CharField(max_length=255,default='')
    file = models.OneToOneField(Media, on_delete= models.CASCADE)
