from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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


urlpatterns = [
    path('admin/', admin.site.urls),

    # Path to direct admin page
    path('admin-need/', include(router.urls)),

    # Swagger URL
    path('Swagger', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),

    # User View of Features
   

    # User View Solution
    path('solution', solutionListView.as_view()),
]
