
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from lstore import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('basket/', include('basket.urls')),
    path('order/', include('order.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
