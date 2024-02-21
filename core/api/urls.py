from django.urls import path
from core.api.views import SignUpView,ProfileView,AddressView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('profile/',ProfileView.as_view()),
    path('address/',AddressView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]