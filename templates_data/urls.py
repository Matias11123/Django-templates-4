from django.contrib import admin
from django.urls import path, include  # <-- Agrega 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil/', include('perfil.urls')),  # <-- Agrega esta línea
]