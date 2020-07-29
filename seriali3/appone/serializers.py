from appone.models import Company, Mobile
from rest_framework import serializers


class MobileSerializer(serializers.ModelSerializer):

    class Meta:
        model=Mobile
        fields="__all__"


class CompanySerializer(serializers.ModelSerializer):
    mob=MobileSerializer(read_only=True , many=True) 
    class Meta:
        model=Company
        fields="__all__"
