from django.contrib import admin
from django.urls import path, include, re_path # re_path is needed for Swagger's regex patterns
from rest_framework import permissions

# Import Swagger-related views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Define the schema view for Swagger
schema_view = get_schema_view(
   # Define basic API information
   openapi.Info(
      title="ALX Travel App API",
      default_version='v1',
      description="API documentation for the ALX Travel App. This provides details on available endpoints, request/response formats, and authentication.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="rafiakedir22@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,), # Allow any user to view the documentation
)

urlpatterns = [
    # Admin URL for Django's built-in administration site
    path('admin/', admin.site.urls),

    # Include URLs from your 'listings' app
    path('api/', include('listings.urls')),

    # URLs for Swagger API documentation (DRF-YASG)
    # These paths serve the OpenAPI schema in JSON and YAML formats, and the interactive UI.

    # This path serves the raw JSON/YAML schema (useful for integrating with other tools)
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # This path serves the interactive Swagger UI (human-readable documentation in browser)
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # This path serves the Redoc UI (another style of API documentation)
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
