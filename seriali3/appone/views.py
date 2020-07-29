from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from appone.models import Company, Mobile
from appone.serializers import MobileSerializer
from appone.serializers import CompanySerializer
from rest_framework.views import APIView
from rest_framework.response import Response



class CompanyView(APIView):
    def get(self,request):
        company=Company.objects.all()
        serializer=CompanySerializer(company, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class MobileView(APIView):
    def get(self,request):
        mobiles=Mobile.objects.all()
        serializer=MobileSerializer(mobiles, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=MobileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
