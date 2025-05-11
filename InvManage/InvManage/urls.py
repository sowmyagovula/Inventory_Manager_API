from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.urls import views as auth_views
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Inventory.urls')),
    path('Inventory/', include('Inventory.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/Inventory/', permanent=False)),


    path("__reload__/", include("django_browser_reload.urls")),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)