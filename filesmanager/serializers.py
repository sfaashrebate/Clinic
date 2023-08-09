from rest_framework import serializers

from filesmanager.models import Media, TestModel

class FileUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model= Media
        fields= ( 'id' , 'file')

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model= TestModel
        fields= ('id' , 'name' , 'file')
