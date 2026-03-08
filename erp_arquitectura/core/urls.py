from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_erp'), 
    # Esta es la línea que activa el botón:
    path('generar-124/', views.generar_formulario_124, name='generar_124'),
]