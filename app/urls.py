from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter

from app.views import TodoViewSet

router = DefaultRouter()
router.register("todos", TodoViewSet)
urlpatterns = router.urls
