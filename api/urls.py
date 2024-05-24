from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from api.views import pickuplinesviewset

router = routers.DefaultRouter()
router.register('pickup', pickuplinesviewset)

urlpatterns = [
    path('', include(router.urls)),
]
