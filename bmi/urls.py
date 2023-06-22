from django.urls import path, include

from bmi.views import BmiViewSet

urlpatterns = [
    path('', BmiViewSet.as_view(),name='bmi' ),
]