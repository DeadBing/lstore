from django.urls import path

from .views import *

urlpatterns = [
    path('', order_create, name='order_create'),
    path('created/', order_created, name='order_created'),
]