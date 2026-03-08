from django.urls import path
from frontend import views as frontend_views
from core import views as core_views

urlpatterns = [
    # Página pública
    path("", frontend_views.index, name="frontend_index"),

    # Panel ERP interno
    path("erp/", core_views.home, name="erp_home"),

    # Automatización de formularios MINVU
    path("formulario_124/", core_views.generar_formulario_124, name="formulario_124"),
    path("debug-pdf/", core_views.debug_campos_pdf, name="debug_pdf"),
]
