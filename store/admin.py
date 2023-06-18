from django.contrib import admin

from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'materials', 'price', 'photo', 'time_create', 'category')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('time_create', 'name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'text')


admin.site.register(Product, ProductAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
