"""
URL configuration for my_optimization project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title="My Optimization API",
        default_version='v1',
        description="API optimization practices",
        terms_of_service="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        contact=openapi.Contact(email="jckkinyanjui@gmail.com"),
        license=openapi.License(name="MIT License"),
        
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
schema_view.with_ui('swagger', cache_timeout=0)
schema_view.with_ui('redoc', cache_timeout=0)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/posts/', include('posts.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
