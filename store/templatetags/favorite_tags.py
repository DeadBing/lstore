from django import template
from store.models import Favorite

register = template.Library()

@register.filter
def is_favorite(product, user):
    return Favorite.objects.filter(user=user, product=product).exists()
