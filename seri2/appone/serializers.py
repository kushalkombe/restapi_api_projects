from appone.models import Book, Chapter
from rest_framework import serializers
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chapter
        fields="__all__"

class BookSerializer(serializers.ModelSerializer):
    chapter=ChapterSerializer(read_only=True , many=True)
    class Meta:
        model=Book
        fields="__all__"
