from django.contrib import admin
from django.urls import path, include
from core import views # Importamos las vistas de core

urlpatterns = [
    path('admin/', admin.site.urls),
    path('erp/', include('core.urls')), 
    # ESTA LÍNEA arregla el error 404 de la página de inicio:
    path('', views.home_erp, name='home'), 
]
