from rest_framework import serializers
from .models import *

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class SubFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubFeature
        fields = '__all__'