from django.urls import path, include
from filesmanager.views import FileUploadViewSet#,TestViewSet
from rest_framework.routers import DefaultRouter

file_router = DefaultRouter()
file_router.register('upload-file',FileUploadViewSet , basename='upload-file')
# file_router.register('test-api',TestViewSet , basename='test-api')

urlpatterns = [
    path('', include(file_router.urls)),
]
