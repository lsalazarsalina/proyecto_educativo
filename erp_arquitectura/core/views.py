from __future__ import annotations
from pathlib import Path
from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from django.conf import settings

# Importaciones de tus servicios locales
from .services.excel_reader import ExcelReader124
from .services.minvu_pdf_filler import rellenar_pdf_124
from pypdf import PdfReader

# Configuración de rutas de archivos
PDF_ORIGINAL = Path(settings.BASE_DIR) / "core" / "static" / "formularios" / "formulario_12_4.pdf"
PDF_OUTPUT_DIR = Path(settings.BASE_DIR) / "core" / "static" / "formularios" / "generados"

def index(request):
    """Página principal de Refugio Nómada"""
    # Si el archivo está en core/templates/index.html, usa 'index.html'
    # Si está en core/templates/core/index.html, usa 'core/index.html'
    return render(request, 'index.html') 

def generar_formulario_124(request):
    """Lógica para procesar el Excel y devolver el PDF rellenado"""
    if request.method == "POST":
        excel_file = request.FILES.get("excel")
        
        if not excel_file:
            return render(request, 'core/home.html' {
                "error": "Debes subir un archivo Excel."
            })

        # Crear directorio de salida si no existe
        PDF_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        tmp_path = PDF_OUTPUT_DIR / "tmp_input.xlsx"
        
        # Guardar archivo temporal
        with open(tmp_path, "wb") as f:
            for chunk in excel_file.chunks():
                f.write(chunk)

        # Leer datos del Excel
        reader = ExcelReader124()
        datos, errores = reader.leer(tmp_path)

        if errores:
            return render(request, "core/formulario_124.html", {
                "errores": errores
            })

        # Generar PDF rellenado
        pdf_salida = PDF_OUTPUT_DIR / "formulario_12_4_rellenado.pdf"
        rellenar_pdf_124(datos, PDF_ORIGINAL, pdf_salida)

        # Retornar el archivo para descarga inmediata
        return FileResponse(
            open(pdf_salida, "rb"),
            content_type="application/pdf",
            as_attachment=True,
            filename="Formulario_12_4_rellenado.pdf",
        )

    # Si entras por primera vez (GET), muestra el formulario
    return render(request, 'core/formulario_124.html')

def debug_campos_pdf(request):
    """Herramienta para ver los nombres técnicos de los campos del PDF"""
    if not PDF_ORIGINAL.exists():
        return HttpResponse(f"Error: No se encuentra el PDF en {PDF_ORIGINAL}", status=404)
        
    reader = PdfReader(PDF_ORIGINAL)
    fields = reader.get_fields()

    texto = "CAMPOS DETECTADOS EN EL PDF:\n" + "="*30 + "\n"
    if fields:
        for name, field in fields.items():
            texto += f"NOMBRE: {name}\nDETALLE: {field}\n" + "-"*50 + "\n"
    else:
        texto += "No se detectaron campos de formulario en este PDF."

    return HttpResponse(texto, content_type="text/plain")