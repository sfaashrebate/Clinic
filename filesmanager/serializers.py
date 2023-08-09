from rest_framework import serializers

from filesmanager.models import Media, TestModel

class FileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model= Media
        fields= '__all__'

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model= TestModel
        fields= ('id' , 'test' , 'file')
