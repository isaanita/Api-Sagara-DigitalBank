from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from featuress.views import *
from partnership.views import *

from solution.views import *

schema_view = get_schema_view(
    openapi.Info(
        title="Sagara Digital Bank API",
        default_version='v1',
        description="API yang digunakan untuk konsum FE sagara digital bank",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@dummy.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()

#Register all api that admin need to input data
router.register(r'admin-features', AdminFeatureView),
router.register(r'admin-sub-features', AdminSubFeatureView),
router.register(r'admin-category-partnership', AdminCategoryPartnerView),
router.register(r'admin-content-partnership', AdminContentPartnerView),

urlpatterns = [
    path('admin/', admin.site.urls),

    # Path to direct admin page
    path('admin-need/', include(router.urls)),

    # Swagger URL
    path('Swagger', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),

    # User View of Features
    path('feature', FeatureListAPI.as_view()),
    re_path('feature/(?P<title>.+)/$',
            FeatureFilterView.as_view()),

    path('sub-feature', SubFeatureListAPI.as_view()),
    re_path('sub-feature/(?P<feature_slug>.+)/$',
            SubFeatureFilterByFeatureView.as_view()),
    re_path('sub-feature/(?P<feature_slug>.+)/(?P<SubFeature_slug>.+)/$',
            SubFeatureDetailView.as_view()),

    # User View of Partnership
    path('category-partnership', CategoryPartnerListAPI.as_view()),
    re_path('category-partnership/(?P<partner_type>.+)/$',
            CategoryPartnerFilterView.as_view()),

    path('content-partnership', ContentPartnerListAPI.as_view()),
    re_path('content-partnership/(?P<categoryPartner_slug>.+)/$',
            ContentPartnerFilterByCategoryPartnerView.as_view()),
    re_path('content-partnership/(?P<categoryPartner_slug>.+)/(?P<contentPartner_slug>.+)/$',
            ContentPartnerDetailView.as_view()),
    
    # User View Solution
    path('solution', solutionListView.as_view()),
]
