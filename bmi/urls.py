from django.urls import path, include

from bmi.views import BmiViewSet

urlpatterns = [
    path('bmi/', BmiViewSet.as_view(),name='bmi' ),
]