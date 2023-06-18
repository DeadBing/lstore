from django.urls import path
from .views import *

urlpatterns = [
    path('', Main.as_view(), name='home'),
    path('category/<int:cid>', ShowCategory.as_view(), name='category'),
    path('product/<int:did>', ProductDetail.as_view(), name='detail'),
    path('search/', Search.as_view(), name='search'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('accounts/register/', Registration.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/<username>', profile, name='profile'),
    path('product/<int:did>/add_to_favorite/', AddToFavoriteView.as_view(), name='add_to_favorite'),
    path('product/<int:did>/remove_from_favorite/', RemoveFromFavoriteView.as_view(), name='remove_from_favorite'),
    path('favorites/', favorite_details, name='favorites'),
    path('add_review/<int:did>/', login_required(AddReviewView.as_view()), name='add_review')
]


