from django.urls import path, include
from app.views import ServiceViewSet,SpecificationViewSet,DoctorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('service', ServiceViewSet, basename='service')
router.register('specification', SpecificationViewSet, basename='specification')
router.register('doctor', DoctorViewSet, basename='doctor')


urlpatterns = [
    path('', include(router.urls), name='token_refresh'),

]