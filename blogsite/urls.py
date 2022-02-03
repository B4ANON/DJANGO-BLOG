from os import stat
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('foodblog.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),


] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)