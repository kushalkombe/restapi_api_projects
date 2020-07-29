from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from firstapp.models import Stu
from firstapp.serializers import StuSerializer


class StuView(APIView):
    def get(self,request):
        data=Stu.objects.all()
        serli=StuSerializer(data,many=True)
        return Response(serli.data)

    def post(self,request):
        data=request.data
        serli=StuSerializer(data=data)
        if serli.is_valid():
            serli.save()
            return Response(serli.data,status=201)
        else:
            return Response({'error':'invalid data'},status=404)


class StuViewId(APIView):
    def get_obj(self,id):
        try:
            data = Stu.objects.get(id=id)
            return data
        except Exception as e:
            return Response({'error':'data is not there for this id'},status=404)

    def get(self,request,id):
        data = self.get_obj(id)
        serli=StuSerializer(data)
        return Response(serli.data)

    def put(self,request,id):
        info=request.data
        data = self.get_obj(id)
        serli=StuSerializer(data,data=info,partial=True)
        if serli.is_valid():
            serli.save()
            print('here')
            return Response({'message':'data is updated'},status=200)
        else:
            return Response({"error":"data is not valid"},status=404)

    def delete(self,request,id):
        data=self.get_obj(id)
        data.delete()
        return Response({"message": "data deleted successfully"}, status=200)
