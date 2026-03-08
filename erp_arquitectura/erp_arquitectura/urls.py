from django.contrib import admin
from django.urls import path, include
from core import views as core_views # Importamos la vista desde core

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name='index'), # Aquí le decimos que use la función index de core
    path('erp/', include('core.urls')), # Aquí conectas con las rutas de tu app
]
