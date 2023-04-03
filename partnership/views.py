from django.shortcuts import render
from .serializer import *
from rest_framework import generics, permissions, viewsets

# Create your views here.

# Admin Need
class AdminCategoryPartnerView(viewsets.ModelViewSet):
    serializer_class = CategoryPartnerSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = CategoryPartner.objects.all()

class AdminContentPartnerView(viewsets.ModelViewSet):
    serializer_class = ContentPartnerSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = ContentPartner.objects.all()


# Feature List API
class CategoryPartnerListAPI(generics.ListAPIView):
    serializer_class = CategoryPartnerSerializer
    queryset = CategoryPartner.objects.all()

# Feature Filtering API
class CategoryPartnerFilterView(generics.ListAPIView):
    serializer_class = CategoryPartnerSerializer

    def get_queryset(self):
        partner_type = self.kwargs['partner_type']
        return CategoryPartner.objects.filter(partner_type=partner_type)

# Sub Feature List API
class ContentPartnerListAPI(generics.ListAPIView):
    serializer_class = ContentPartnerSerializer
    queryset = ContentPartner.objects.all()

# Sub Feature Filter by Feature API
class ContentPartnerFilterByCategoryPartnerView(generics.ListAPIView):
    serializer_class = ContentPartnerSerializer

    def get_queryset(self):
        categoryPartner_slug = self.kwargs['categoryPartner_slug']
        return ContentPartner.objects.filter(categoryPartner_slug=categoryPartner_slug)

# Sub Feature Detail by Feature and Sub Feature title API
class ContentPartnerDetailView(generics.ListAPIView):
    serializer_class = ContentPartnerSerializer

    def get_queryset(self):
        categoryPartner_slug = self.kwargs['categoryPartner_slug']
        contentPartner_slug = self.kwargs['contentPartner_slug']
        return ContentPartner.objects.filter(categoryPartner_slug=categoryPartner_slug, contentPartner_slug=contentPartner_slug)