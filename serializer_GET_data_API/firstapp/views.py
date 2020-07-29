from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from firstapp.models import  Emp
from firstapp.serializers import EmpSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# using viewsets
class EmpView(viewsets.ModelViewSet):
        queryset = Emp.objects.all()
        serializer_class = EmpSerializer


# using apiview
class EmpViewApi(APIView):
        def get(self,request):
            data = Emp.objects.all()
            serialdata = EmpSerializer(data,many=True)
            return Response(serialdata.data)
