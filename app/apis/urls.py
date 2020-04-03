"""authors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.conf.urls import url
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions

schema_view_ = get_schema_view(
    openapi.Info(
        title="Mpesa Test API",
        default_version='v1',
        description="Documentation for Mpesa Test API"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
swagger_ui_view = get_swagger_view()

urlpatterns = [
    url(r'^docs/$', schema_view_.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    url(r'^docs(?P<format>\.json|\.yaml)$', schema_view_.without_ui(
        cache_timeout=0), name='schema-json'),
    url(r'^redoc/$', schema_view_.with_ui('redoc',
                                          cache_timeout=0), name='schema-redoc'),
    url(r'^docs/$', swagger_ui_view),
    path('mpesa/', include(('app.apis.mpesa.urls', 'mpesa'), namespace='payment')),
    path('users/', include(('app.apis.authentication.urls', 'authentication'), namespace='authentication')),

]
