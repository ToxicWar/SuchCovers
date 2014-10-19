# coding: utf-8
from __future__ import unicode_literals
from site_such_covers.app.api.views import CoverViewSet, NotebookViewSet
from django.conf.urls import url, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'covers', CoverViewSet)
router.register(r'notebooks', NotebookViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
