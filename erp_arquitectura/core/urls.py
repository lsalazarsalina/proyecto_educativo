from django.urls import path
from . import views  # Esto importa las vistas de la misma carpeta core

urlpatterns = [
    path('', views.home_erp, name='home_erp'),
    path('generar/', views.generar_formulario_124, name='formulario_124'),
    path('debug-pdf/', views.debug_campos_pdf, name='debug_pdf'),
]
