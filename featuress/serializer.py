from rest_framework import serializers
from .models import *

class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = '__all__'

class SubFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubFeatures
        fields = '__all__'

class BenefitFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenefitFeatures
        fields = '__all__'