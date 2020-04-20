from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('accounts/',include('allauth.urls')),
    path('admin/', admin.site.urls),
]
