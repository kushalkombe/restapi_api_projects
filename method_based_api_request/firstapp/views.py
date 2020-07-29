from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from firstapp.models import Emp
from firstapp.serializers import EmpSerializer
from rest_framework.response import Response
from rest_framework.parsers import  JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt


@csrf_exempt
def emp(request):
    if request.method == "GET":
        query_set = Emp.objects.all()
        seril = EmpSerializer(query_set,many=True)
        return JsonResponse(seril.data,safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        res = EmpSerializer(data=data)
        if res.is_valid():
            res.save()
            return JsonResponse(res.data,status=201)


@csrf_exempt
def emp_details(request,id):
    if request.method == 'GET':
        try:
            Emp.objects.get(id=id)
            query_set = Emp.objects.get(id=id)
            seril = EmpSerializer(query_set)
        except Exception as e:
            return JsonResponse({'error':'no data for id'},status=404)
        return JsonResponse(seril.data,safe=False)

    elif request.method == "PUT":
        try:
            Emp.objects.get(id=id)
            query_set = Emp.objects.get(id=id)

            data = JSONParser().parse(request)
            res = EmpSerializer(query_set,data=data,partial=True)
            if res.is_valid():
                res.save()
                return JsonResponse(res.data, status=201)
        except Exception as e:
            return JsonResponse({'error': 'no data for id'}, status=404)
        return JsonResponse(res.data, safe=False)

    elif request.method=='DELETE':
        try:
            Emp.objects.get(id=id)
            query_set = Emp.objects.get(id=id)
            query_set.delete()
            return JsonResponse({'data':'deleted successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': 'no data for id'}, status=404)
        return JsonResponse(res.data, safe=False)
