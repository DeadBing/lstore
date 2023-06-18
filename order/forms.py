from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'street', 'house', 'city', 'region', 'index', 'country', 'phone_number']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'street': 'Улица',
            'house': 'Дом. корпус. квартира',
            'city': 'Город',
            'region': 'Область',
            'index': 'Индекс',
            'country': 'Страна',
            'phone_number': 'Номер телефона'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={"class":"form-control order-form-input", "id":"form1"}),
            'last_name': forms.TextInput(attrs={"class":"form-control order-form-input", "id":"form2"}),
            'street': forms.TextInput(attrs={"class":"form-control order-form-input", "id":"form5"}),
            'house': forms.TextInput(attrs={"class":"form-control order-form-input", "id":"form6"}),
            'city': forms.TextInput(attrs={"class":"form-control order-form-input", "id":"form8"}),
            'region': forms.TextInput(attrs={"class":"form-control order-form-input", "id":"form9"}),
            'index': forms.TextInput(attrs={"class":"form-control order-form-input", "id":"form10"}),
            'country': forms.TextInput(attrs={"class":"form-control order-form-input", "id":"form11"}),
            'phone_number': forms.TextInput(attrs={"class":"form-control order-form-input", "id":"form3"}),

        }