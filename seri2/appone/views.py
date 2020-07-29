from django.shortcuts import render
from appone.models import Book, Chapter
from appone.serializers import BookSerializer
from appone.serializers import ChapterSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class BookView(APIView):
    def get(self,request):
        books=Book.objects.all()
        serializer=BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ChapterView(APIView):
    def get(self,request):
        chapters=Chapter.objects.all()
        serializer=ChapterSerializer(chapters, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ChapterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
