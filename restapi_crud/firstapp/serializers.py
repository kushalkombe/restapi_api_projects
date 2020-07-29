from rest_framework import serializers
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.HyperLinkedModelSerializers):
    class Meta:
        model=User
        fields = (
        'first_name',
        'last_name',
        'email',
        'url'
        )
