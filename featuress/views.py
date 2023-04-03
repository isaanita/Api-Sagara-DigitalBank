from django.shortcuts import render
from .serializer import *
from rest_framework import generics, permissions, viewsets

# Create your views here.

# Admin Need
class AdminFeatureView(viewsets.ModelViewSet):
    serializer_class = FeatureSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = Feature.objects.all()

class AdminSubFeatureView(viewsets.ModelViewSet):
    serializer_class = SubFeatureSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = SubFeature.objects.all()


# Feature List API
class FeatureListAPI(generics.ListAPIView):
    serializer_class = FeatureSerializer
    queryset = Feature.objects.all()

# Feature Filtering API
class FeatureFilterView(generics.ListAPIView):
    serializer_class = FeatureSerializer

    def get_queryset(self):
        title = self.kwargs['title']
        return Feature.objects.filter(title=title)

# Sub Feature List API
class SubFeatureListAPI(generics.ListAPIView):
    serializer_class = SubFeatureSerializer
    queryset = SubFeature.objects.all()

# Sub Feature Filter by Feature API
class SubFeatureFilterByFeatureView(generics.ListAPIView):
    serializer_class = SubFeatureSerializer

    def get_queryset(self):
        feature_slug = self.kwargs['feature_slug']
        return SubFeature.objects.filter(feature_slug=feature_slug)

# Sub Feature Detail by Feature and Sub Feature title API
class SubFeatureDetailView(generics.ListAPIView):
    serializer_class = SubFeatureSerializer

    def get_queryset(self):
        feature_slug = self.kwargs['feature_slug']
        SubFeature_slug = self.kwargs['SubFeature_slug']
        return SubFeature.objects.filter(feature_slug=feature_slug, SubFeature_slug=SubFeature_slug)