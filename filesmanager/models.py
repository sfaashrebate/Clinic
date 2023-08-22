from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

def upload_profile_image_location(instance, filename, **kwargs):
	file_path = '/'.join(['images', filename])
    
	return file_path


class Media(models.Model):
    file = models.FileField(
            default=None,
            null=True,
            blank=True,
            upload_to=upload_profile_image_location,
            validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg', 'png'])]
    )

# class TestModel(models.Model):
#     test = models.CharField(max_length=255,default='')
#     file = models.OneToOneField(Media, on_delete= models.CASCADE)
