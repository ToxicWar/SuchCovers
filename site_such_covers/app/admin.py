# coding: utf-8
from django.contrib import admin
from site_such_covers.app.models import Notebook, Cover, Order, OrderItem


admin.site.register(Notebook)
admin.site.register(Cover)
admin.site.register(Order)
admin.site.register(OrderItem)
