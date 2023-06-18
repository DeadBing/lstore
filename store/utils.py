from .models import *

class CategoryMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        categorys = Category.objects.all()
        context['categorys'] = categorys
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context