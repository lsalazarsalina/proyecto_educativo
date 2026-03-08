from __future__ import annotations
from pathlib import Path
from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from django.conf import settings

# Importaciones unificadas (Asegúrate de que la carpeta sea 'frontend' o 'core')
try:
    from frontend.services.excel_reader import ExcelReader124
    from frontend.services.minvu_pdf_filler import rellenar_pdf_124
except ImportError:
    from core.frontend.services.excel_reader import ExcelReader124
    from core.frontend.services.minvu_pdf_filler import rellenar_pdf_124

from pypdf import PdfReader

# --- CONFIGURACIÓN DE RUTAS ---
# Estas variables son vitales para que no salga pantalla en blanco
BASE_DIR = Path(settings.BASE_DIR)
PDF_OUTPUT_DIR = BASE_DIR / "media" / "generados"
# Asegúrate de que el PDF original esté en esta ruta:
PDF_ORIGINAL = BASE_DIR / "static" / "pdf" / "formulario_124_original.pdf"

def home_erp(request):
    """Vista principal del ERP"""
    return render(request, "core/formulario_124.html")

def generar_formulario_124(request):
    if request.method == "POST":
        excel_file = request.FILES.get("excel")
        if not excel_file:
            return render(request, "core/formulario_124.html", {"error": "Debes subir un archivo Excel."})

        # Crear directorio si no existe
        PDF_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        tmp_path = PDF_OUTPUT_DIR / "tmp_input.xlsx"
        
        with open(tmp_path, "wb") as f:
            for chunk in excel_file.chunks():
                f.write(chunk)

        reader = ExcelReader124()
        datos, errores = reader.leer(tmp_path)

        if errores:
            return render(request, "core/formulario_124.html", {"errores": errores})

        # Verificar si el PDF original existe antes de intentar rellenar
        if not PDF_ORIGINAL.exists():
            return render(request, "core/formulario_124.html", {"error": f"No se encontró el PDF original en {PDF_ORIGINAL}"})

        pdf_salida = PDF_OUTPUT_DIR / "formulario_12_4_rellenado.pdf"
        rellenar_pdf_124(datos, str(PDF_ORIGINAL), str(pdf_salida))

        return FileResponse(
            open(pdf_salida, "rb"),
            content_type="application/pdf",
            as_attachment=True,
            filename="Formulario_12_4_rellenado.pdf",
        )

    return render(request, "core/formulario_124.html")

def debug_campos_pdf(request):
    """Útil para ver los nombres de los campos del PDF del MINVU"""
    if not PDF_ORIGINAL.exists():
        return HttpResponse(f"Archivo no encontrado en: {PDF_ORIGINAL}")
        
    reader = PdfReader(PDF_ORIGINAL)
    fields = reader.get_fields()

    texto = f"Analizando: {PDF_ORIGINAL}\n" + "="*50 + "\n"
    if not fields:
        texto += "No se encontraron campos editables en este PDF."
    else:
        for name, field in fields.items():
            texto += f"NOMBRE DEL CAMPO: {name}\n"
            texto += f"TIPO/DETALLE: {field}\n"
            texto += "-" * 50 + "\n"

    return HttpResponse(texto, content_type="text/plain")