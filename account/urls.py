from django.urls import path, include
from account.views import (
    AccountViewSet,
    registration_view,
    #account_properties_view,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

profile_router = DefaultRouter()
profile_router.register('profile', AccountViewSet, basename='profile')

urlpatterns = [
    path('registration/', registration_view),
    path('', include(profile_router.urls),name='profile' ),
    # path('/', account_properties_view, name='token_refresh'),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', registration_view),

]