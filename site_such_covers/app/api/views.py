# coding: utf-8
from __future__ import unicode_literals
from site_such_covers.app.api.serializers import CoverSerializer, NotebookSerializer
from site_such_covers.app.models import Cover, Notebook
from rest_framework import viewsets


class CoverViewSet(viewsets.ModelViewSet):
    model = Cover
    serializer_class = CoverSerializer


class NotebookViewSet(viewsets.ModelViewSet):
    model = Notebook
    serializer_class = NotebookSerializer
