from django.urls import re_path, path
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Magnat API",
      default_version='v1.0',
      description="Official web site for Magnat IT Comapany",
      terms_of_service="https://t.me/Rozievich",
      contact=openapi.Contact(email="oybekrozievich@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('site/admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]