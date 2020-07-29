from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views  import APIView
from rest_framework.response import Response
from firstapp.serializers import NameSerializer

class APIView(APIView):
    def get(self,request,*args,**kwargs):
        color=['RED','YELLOW','GREEN']
        return Response({"colors":color,"msg":"hello"}) # return Response will convert python Dict to Json

    def post(self,request,*args,**kwargs):
        serializer=NameSerializer(data=request.data)  #this will convert json to python ...request.data is coming from partner appn
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='hello {}, happy pongal'.format(name)
            return Response({'msg':msg})
        else:
            return Response (serializer.errors,status=400)

    def put(self,request,*args,**kwargs):
        return Response("this is from put request")

    def  patch(self,request,*args,**kwargs):
        return Response("this is from patch request")

    def delete(self,request):
        return Response("this is from delete request")

# ViewSets

from rest_framework.viewsets import ViewSet

class ViewSet(ViewSet):
    def list(self,request):
        colors=['RED','ORANGE','YELLOW','GREEN']
        return Response({"msg":"hello","colours":colors})

    def create(self,request):
        serializer=NameSerializer(data=request.data)  #this will convert json to python ...request.data is coming from partner appn
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='hello {}, happy pongal'.format(name)
            return Response({'msg':msg})
        else:
            return Response (serializer.errors,status=400)

    def retrive(self,request,pk=None):
        return Response({'msg':"this is retrive method of viewset"})

    def update(self,request,pk=None):
        return Response({'msg':'this is update method of viewset'})
    def partial_update(self,request,pk=None):
        return Response({'msg':'this is partial_update method of viewset'})
    def destroy(self,request,pk=None):
        return Response({'msg':'this is destroy method of viewset'})
