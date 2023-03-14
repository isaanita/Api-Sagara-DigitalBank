from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from featuress.views import *

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
router.register(r'admin-features', AdminFeaturesView),
router.register(r'admin-sub-features', AdminSubFeaturesView),
router.register(r'admin-benefit-features', AdminBenefitFeaturesView),

urlpatterns = [
    path('admin/', admin.site.urls),

    # Path to direct admin page
    path('admin-need/', include(router.urls)),

    # Swagger URL
    path('Swagger', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),

    # User View of Features
    path('features', FeaturesListAPI.as_view()),
    re_path('features/(?P<features_title>.+)/$',
            FeatureFilterAPI.as_view()),

    path('sub-features', SubFeatureListAPI.as_view()),
    re_path('sub-features/(?P<features_slug>.+)/$',
            SubFeaturesFilterByFeaturesView.as_view()),
    re_path('features/(?P<features_slug>.+)/(?P<sub_features_slug>.+)/$',
            SubFeaturesDetailView.as_view()),

    path('benefit-features', BenefitFeaturesListAPI.as_view()),
    re_path('benefit_features/(?P<sub_features_slug>.+)/$',
            BenefitFeaturesBySubFeaturesView.as_view()),
    re_path('sub_features/(?P<sub_features_slug>.+)/(?P<benefit_features_slug>.+)/$',
            BenefitFeaturesDetailView.as_view()),
    


    # User View Solution
    path('solution', solutionListView.as_view()),
]
