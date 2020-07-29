from django.shortcuts import render,redirect
from appone.models import *
from appone.forms import *
from django.views import View
from appone.forms import UserRegistrationForm
# Create your views here.



class Fetchs(View):
    def get(self,request):
        obj=Student.objects.all()
        return render(request,'appone/sindex.html',{'obj':obj})

class Adds(View):
    def get(self,request):
        form=StudentForm()
        return render(request,'appone/sadd.html',{'form':form})
    def post(self,request):
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sindex/')
        return render(request,'appone/sadd.html')

class Deletes(View):
    def get(self,request,**kwargs):
        id=kwargs.get('id')
        obj=Student.objects.get(pk=id)
        obj.delete()
        return redirect('/sindex/')

class Updates(View):
    def get(self,request,id):
        obj=Student.objects.get(pk=id)
        form=StudentForm(instance=obj)
        return render(request,'appone/supdate.html',{'form':form,'obj':obj})

    def post(self,request,**kwargs):
        id=kwargs.get('id')
        obj=Student.objects.get(pk=id)
        form=StudentForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return redirect('/sindex/')
