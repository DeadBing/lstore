from django.contrib.auth.models import User
from django.db import models
from store.models import *


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='Заказы')
    time_create = models.DateField(auto_now_add=True, null=True)
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    street = models.CharField(max_length=20, verbose_name='Улица')
    house = models.CharField(max_length=20, verbose_name='Дом')
    city = models.CharField(max_length=20, verbose_name='Город')
    region = models.CharField(max_length=20, verbose_name='Область')
    index = models.CharField(max_length=12, verbose_name='Индекс')
    country = models.CharField(max_length=20, verbose_name='Страна')
    phone_number = models.TextField(max_length=200, null=True, verbose_name='Номер телефона')
    updated = models.DateTimeField(auto_now=True)


    def __int__(self):
        return self.pk

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT, verbose_name='Отношение к заказу')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT, verbose_name='Что заказано')
    price = models.IntegerField(verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    size = models.CharField(max_length=3, verbose_name='Размер', default='XS')

    class Meta:
        verbose_name = 'Заказанный товар'
        verbose_name_plural = 'Заказанные товары'

    def __int__(self):
        return self.pk

    def get_cost(self):
        return self.price * self.quantity