from rest_framework import serializers
from .models import *

class CategoryPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPartner
        fields = '__all__'

class ContentPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentPartner
        fields = '__all__'