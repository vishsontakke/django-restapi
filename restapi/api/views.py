from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

#for react login and logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
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


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)