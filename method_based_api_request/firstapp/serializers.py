from rest_framework import serializers
from firstapp.models import Emp

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = '__all__'
