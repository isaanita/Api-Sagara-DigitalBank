from django.shortcuts import render
from .serializer import *
from rest_framework import generics, permissions, viewsets

# Create your views here.

# Admin Need
class AdminFeaturesView(viewsets.ModelViewSet):
    serializer_class = FeaturesSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = Features.objects.all()

class AdminSubFeaturesView(viewsets.ModelViewSet):
    serializer_class = SubFeatureSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = SubFeatures.objects.all()

class AdminBenefitFeaturesView(viewsets.ModelViewSet):
    serializer_class = BenefitFeatureSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = BenefitFeatures.objects.all()


# Features List API
class FeaturesListAPI(generics.ListAPIView):
    serializer_class = FeaturesSerializer
    queryset = Features.objects.all()

# Features Filtering API
class FeatureFilterAPI(generics.ListAPIView):
    serializer_class = FeaturesSerializer

    def get_queryset(self):
        features_title = self.kwargs['features_title']
        return Features.objects.filter(features_title=features_title)

# Sub Features List API
class SubFeatureListAPI(generics.ListAPIView):
    serializer_class = SubFeatureSerializer
    queryset = SubFeatures.objects.all()

# Sub Features Filtering API
class SubFeaturesFilterAPI(generics.ListAPIView):
    serializer_class = SubFeatureSerializer

    def get_queryset(self):
        sub_features_title = self.kwargs['sub_features_title']
        return SubFeatures.objects.filter(sub_features_title=sub_features_title)

# Sub Features Filter by Features API
class SubFeaturesFilterByFeaturesView(generics.ListAPIView):
    serializer_class = SubFeatureSerializer

    def get_queryset(self):
        features_slug = self.kwargs['features_slug']
        return SubFeatures.objects.filter(features_slug=features_slug)

# Sub Features Detail by Features and Sub Features title API
class SubFeaturesDetailView(generics.ListAPIView):
    serializer_class = SubFeatureSerializer

    def get_queryset(self):
        features_slug = self.kwargs['features_slug']
        sub_features_slug = self.kwargs['sub_features_slug']
        return SubFeatures.objects.filter(features_slug=features_slug, sub_features_slug=sub_features_slug)

# Benefit Features List API
class BenefitFeaturesListAPI(generics.ListAPIView):
    serializer_class = BenefitFeatureSerializer
    queryset = BenefitFeatures.objects.all()

# Benefit Features Filtering API
class BenefitFeaturesFilterAPI(generics.ListAPIView):
    serializer_class = BenefitFeatureSerializer
    
    def get_queryset(self):
        title = self.kwargs['title']
        return BenefitFeatures.objects.filter(title=title)
    
# Benefit Features Filter by Sub Features API
class BenefitFeaturesBySubFeaturesView(generics.ListAPIView):
    serializer_class = BenefitFeatureSerializer

    def get_queryset(self):
        sub_features_slug = self.kwargs['sub_features_slug']
        return BenefitFeatures.objects.filter(sub_features_slug=sub_features_slug)
    
# Benefit Features Detail by Sub Features and Benefit Features title API
class BenefitFeaturesDetailView(generics.ListAPIView):
    serializer_class = BenefitFeatureSerializer

    def get_queryset(self):
        sub_features_slug = self.kwargs['sub_features_slug']
        benefit_features_slug = self.kwargs['benefit_features_slug']
        return BenefitFeatures.objects.filter(sub_features_slug=sub_features_slug, benefit_features_slug=benefit_features_slug)