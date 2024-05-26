from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies',CompanyViewSet,basename='company')
router.register(r'employee',EmployeeViewSet,basename='employee')


urlpatterns = [
    path('',include(router.urls))
]