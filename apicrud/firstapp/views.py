from django.shortcuts import render

# Create your views here.

import rest_framework
from rest_framework import generics
from firstapp.models import *
from firstapp.serializers import *
# Create your views here.
from rest_framework import mixins
class EmployeeListModelMixin(mixins.CreateModelMixin,generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class EmployeeDetailAPIViewMixin(mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.RetrieveAPIView):
        queryset=Employee.objects.all()
        serializer_class=EmployeeSerializer
        def put(self,request,*args,**kwargs):
            return self.update(request,*args,**kwargs)
        def patch(self,request,*args,**kwargs):
            return self.partial_update(request,*args,**kwargs)
        def delete(self,request,*args,**kwargs):
            return self.destroy(request,*args,**kwargs)
