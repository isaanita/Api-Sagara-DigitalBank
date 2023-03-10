from django.shortcuts import render
from .serializer import *
from rest_framework import generics, viewsets,permissions

# Create your views here.

# ADMIN NEED
class featuresAdminView(viewsets.ModelViewSet):
    serializer_class = featuresSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = features.objects.all()


# Features List API
class featuresListView(generics.ListAPIView):
    serializer_class = featuresSerializer
    queryset = features.objects.all()

