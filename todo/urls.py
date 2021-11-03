from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from app import urls as app_url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include((app_url, 'api'), namespace='any')),
]
