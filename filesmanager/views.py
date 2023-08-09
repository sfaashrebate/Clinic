
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser

from filesmanager.models import Media, TestModel
from filesmanager.serializers import FileUploadSerializer,TestSerializer


class FileUploadViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = [MultiPartParser,]


class TestViewSet(ModelViewSet):
    """
    file -> id of file object.
    """
    queryset= TestModel.objects.all()
    serializer_class = TestSerializer

