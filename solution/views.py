from django.shortcuts import render
from .serializer import *
from rest_framework import viewsets, generics, permissions

class solutionAdminView(viewsets.ModelViewSet):
    serializer_class = solutionSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = solution.objects.all()

class solutionListView(generics.ListAPIView):
    serializer_class = solutionSerializer
    queryset = solution.objects.all()