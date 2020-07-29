from django.shortcuts import render

# Create your views here.

#from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from firstapp.serializers import *
from firstapp.models import *
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,
DjangoModelPermissionsOrAnonReadOnly
from firstapp.permission import IsGETorPatch ,IsReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
class EmployeeCRUDCBV(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class =EmployeeSerializer
    #authentication_classes=[JSONWebTokenAuthentication,]
    # authentication_classes=[TokenAuthentication,]
    authentication_classes=[SessionAuthentication,]
    permission_classes=[IsAdminUser,]
    #permission_classes=[AllowAny,]#IsAuthenticated
    # permission_classes=[IsGETorPatch,]
    # permission_classes=[IsAuthenticated,]
