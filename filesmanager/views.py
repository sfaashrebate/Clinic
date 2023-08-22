
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser

from filesmanager.models import Media#, TestModel
from filesmanager.serializers import FileUploadSerializer#,TestSerializer
from rest_framework.permissions import IsAuthenticated

class FileUploadViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = [MultiPartParser,]
    permission_classes = [IsAuthenticated]

# class TestViewSet(ModelViewSet):
#     """
#     file -> id of file object.
#     """
#     queryset= TestModel.objects.all()
#     serializer_class = TestSerializer

