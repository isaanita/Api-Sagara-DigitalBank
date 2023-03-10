from rest_framework import serializers
from .models import *

class solutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = solution
        fields = '__all__'