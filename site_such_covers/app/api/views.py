# coding: utf-8
from __future__ import unicode_literals
from site_such_covers.app.api.serializers import CoverSerializer, NotebookSerializer, OrderSerializer, OrderItemSerializer
from site_such_covers.app.models import Cover, Notebook, Order, OrderItem
from rest_framework import viewsets


class CoverViewSet(viewsets.ModelViewSet):
    model = Cover
    serializer_class = CoverSerializer

    def get_queryset(self):
        qs = super(CoverViewSet, self).get_queryset()
        return qs.filter(is_display=True)


class NotebookViewSet(viewsets.ModelViewSet):
    model = Notebook
    serializer_class = NotebookSerializer


class OrderViewSet(viewsets.ModelViewSet):
    model = Order
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    model = OrderItem
    serializer_class = OrderItemSerializer
