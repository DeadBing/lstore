from django import forms

SIZES = [
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
]

class AddBasketForm(forms.Form):
    quantity = forms.IntegerField(label="Количество", min_value=1, widget=forms.NumberInput(attrs={"class":"form-control form-control-lg form-width"}))
    size = forms.TypedChoiceField(label='Размер', choices=SIZES, widget=forms.Select(attrs={"class":"form-control form-control-lg form-width"}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)