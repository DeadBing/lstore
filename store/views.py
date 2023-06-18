from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views import View
from django.views.generic import ListView, CreateView
from .models import *
from .utils import *
from .forms import *
from basket.forms import *
from order.models import *


class Main(CategoryMixin, ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category_mixin = self.get_user_context(title="Главная страница")
        context = dict(list(context.items()) + list(category_mixin.items()))
        return context

    def get_queryset(self):
        return Product.objects.all()


class ShowCategory(CategoryMixin, ListView):
    model = Product
    template_name = 'store/products.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category_mixin = self.get_user_context()
        context['title'] = 'Категория: ' + str(Category.objects.get(id=self.kwargs['cid']))
        context = dict(list(context.items()) + list(category_mixin.items()))
        return context

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['cid'])

class AddToFavoriteView(View):
    def get(self, request, did, *args, **kwargs):
        product = get_object_or_404(Product, pk=did)
        favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)
        return redirect('detail', did=did)

@login_required
def favorite_details(request):
    user = request.user
    user_favorites = reversed(Favorite.objects.filter(user=request.user))
    user_favorites_length = Favorite.objects.filter(user=request.user)
    categorys = Category.objects.all()
    context = {
        'user': user,
        'user_favorites': user_favorites,
        'user_favorites_length': user_favorites_length,
        'title': 'Избранное',
        'categorys': categorys,
    }
    return render(request, 'store/favorite_detail.html', context)

class RemoveFromFavoriteView(View):
    def get(self, request, did, *args, **kwargs):
        product = get_object_or_404(Product, pk=did)
        Favorite.objects.filter(user=request.user, product=product).delete()
        return redirect('detail', did=did)

class ProductDetail(CategoryMixin, ListView):
    model = Product
    template_name = 'store/single-product.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddBasketForm()
        context['form_review'] = ReviewForm()
        context['reviews'] = reversed(Review.objects.filter(product=Product.objects.get(id=self.kwargs['did'])))
        category_mixin = self.get_user_context()
        context['title'] = Product.objects.get(id=self.kwargs['did'])
        context = dict(list(context.items()) + list(category_mixin.items()))
        return context

    def get_queryset(self):
        return Product.objects.get(id=self.kwargs['did'])

class AddReviewView(View):
    def get(self, request, did):
        form = ReviewForm()
        return render(request, 'store/single-product.html', {'form': form})

    def post(self, request, did):
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user
            product = Product.objects.get(id=did)
            text = form.cleaned_data['text']
            review = Review.objects.create(user=user, product=product, text=text)
            return redirect('detail', did=did)
        return render(request, 'store/single-product.html', {'form': form})


class Search(ListView, CategoryMixin):
    template_name = 'store/search.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Поиск'
        category_mixin = self.get_user_context()
        context['q'] = self.request.GET.get('q')
        context = dict(list(context.items()) + list(category_mixin.items()))
        return context

    def get_queryset(self):
        return Product.objects.filter(name__iregex=self.request.GET.get('q'))


class Login(LoginView, CategoryMixin):
    form_class = LoginUserForm
    template_name = 'store/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category_mixin = self.get_user_context()
        context['title'] = "Авторизация"
        context = dict(list(context.items()) + list(category_mixin.items()))
        return context

    def get_success_url(self):
        return reverse_lazy('home')

def logout_view(request):
    logout(request)
    return redirect('home')

class Registration(CreateView, CategoryMixin):
    form_class = RegisterUserForm
    template_name = 'store/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация"
        category_mixin = self.get_user_context()
        context = dict(list(context.items()) + list(category_mixin.items()))
        return context

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

@login_required
def profile(request, username):
        user = request.user
        user_orders = reversed(Order.objects.filter(customer=request.user))
        user_order_item = OrderItem.objects.all()
        categorys = Category.objects.all()
        data = {
            'user': user,
            'user_orders': user_orders,
            'user_order_item': user_order_item,
            'title': 'Профиль',
            'categorys': categorys,
        }
        return render(request, 'store/profile.html', data)


