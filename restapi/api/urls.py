from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from api.views import LogoutView

router = routers.DefaultRouter()
router.register(r'companies',CompanyViewSet,basename='company')
router.register(r'employee',EmployeeViewSet,basename='employee')


urlpatterns = [
    path('',include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]