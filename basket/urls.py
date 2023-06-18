from django.urls import path

from .views import *

urlpatterns = [
    path('', basket_detail, name='basket_detail'),
    path('add/<int:did>', basket_add, name='basket_add'),
    path('remove/<int:did>', basket_remove, name='basket_remove'),
]
