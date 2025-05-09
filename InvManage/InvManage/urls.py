from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.urls import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('Inventory/', include('Inventory.urls')),
    path('accounts/',include('django.contrib.auth.urls')),


    path("__reload__/", include("django_browser_reload.urls")),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)