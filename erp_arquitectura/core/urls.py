from django.urls import path
from .frontend import views as frontend_views
from . import views as core_views

urlpatterns = [
    path("", frontend_views.index_frontend, name="frontend_index"),
    path("erp/", core_views.home_erp, name="erp_home"),
    path("formulario_124/", core_views.generar_formulario_124, name="formulario_124"),
]
