from decimal import Decimal
from django.conf import settings
from store.models import Product

SIZES = [
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
]


class Basket(object):

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def add(self, product, quantity=1, size='XS', update_quantity=False, update_size=False):
        product_id = str(product.id)
        key = f"{product_id}_{size}"
        if key not in self.basket:
            self.basket[key] = {'quantity': 0,
                                'size': size,
                                'price': str(product.price)}
        if update_quantity:
            self.basket[key]['quantity'] = quantity
        else:
            self.basket[key]['quantity'] += quantity

        if update_size:
            self.basket[key]['size'] = size

        self.save()

    def remove(self, product, size='XS'):
        product_id = str(product.id)
        key = f"{product_id}_{size}"
        if key in self.basket:
            del self.basket[key]
            self.save()
#2112
    def __iter__(self):
        product_ids = [key.split('_')[0] for key in self.basket.keys()]
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            for size in SIZES:
                key = f"{str(product.id)}_{size[0]}"
                if key in self.basket:
                    self.basket[key]['product'] = product
        for item in self.basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())

    def save(self):
        self.session[settings.BASKET_SESSION_ID] = self.basket
        self.session.modified = True

    def clear(self):
        del self.session[settings.BASKET_SESSION_ID]
        self.session.modified = True