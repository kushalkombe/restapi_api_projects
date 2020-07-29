from rest_framework import serializers
from .models import Book, Chapters


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapters
        fields = "__all__"


def multiple_of_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')


class BookSerializer(serializers.ModelSerializer):
    chapter_in_book = ChapterSerializer(read_only=True, many=True, )
    

    class Meta:
        model = Book
        fields = "__all__"

    def validate_author(self, value):

        if 'django' not in value.lower():
            raise serializers.ValidationError("author must be string")
        return value

    def validate(self, data):
        if data["title"] != data["subtitle"]:
            raise serializers.ValidationError("title and subtitle must be same")
        return data
