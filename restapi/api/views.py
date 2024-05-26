from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

#companies/{id}/employees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emp = Employee.objects.filter(company=company)
            emp_seriliazers = EmployeeSerializer(emp,many= True, context = {'request':request})
            print("getting employees of" + pk)
            return Response(emp_seriliazers.data)
        except Exception as e:
            return Response({
                'message':"Company not Exists"
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer