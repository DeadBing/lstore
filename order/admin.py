from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'price', 'quantity', 'size']
    list_filter = ['id', 'order']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'time_create', 'first_name', 'last_name', 'street', 'house', 'city', 'region', 'index', 'country', 'phone_number']
    list_filter = ['id', 'first_name']

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)