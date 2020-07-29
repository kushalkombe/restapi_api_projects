from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book, Chapters
from .serializers import BookSerializer, ChapterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response




class BookView(APIView):

    def get(self, request):
        books = Book.objects.get(id=1)
        serializer = BookSerializer(books, many=False)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        instance = Book.objects.get(id=pk)
        serializer = BookSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ChapterViews(APIView):
    def get(self, request):
        chapters = Chapters.objects.all()
        print(chapters)
        serializer = ChapterSerializer(chapters, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChapterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
