from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('reservas/', include('reservas.urls')),
    path('stands/', include('stands.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)