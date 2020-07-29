from rest_framework import serializers
from firstapp.models import Stu

class StuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stu
        fields="__all__"
