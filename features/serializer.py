from rest_framework import serializers
from .models import *

class featuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = features
        fields = '__all__'