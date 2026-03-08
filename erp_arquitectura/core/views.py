from __future__ import annotations
from pathlib import Path
from django.shortcuts import render

def home(request):
    return render(request, "frontend/index.html")

from django.http import FileResponse
from django.conf import settings
from .services.excel_reader import ExcelReader124
from .services.minvu_pdf_filler import rellenar_pdf_124

PDF_ORIGINAL  = Path(settings.BASE_DIR) / "core/static/formularios/formulario_12_4.pdf"
PDF_OUTPUT_DIR = Path(settings.BASE_DIR) / "core/static/formularios/generados"


def home(request):
    return render(request, "core/home.html")


def generar_formulario_124(request):
    if request.method == "POST":
        excel_file = request.FILES.get("excel")
        if not excel_file:
            return render(request, "core/formulario_124.html", {"error": "Debes subir un archivo Excel."})

        PDF_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        tmp_path = PDF_OUTPUT_DIR / "tmp_input.xlsx"
        with open(tmp_path, "wb") as f:
            for chunk in excel_file.chunks():
                f.write(chunk)

        reader = ExcelReader124()
        datos, errores = reader.leer(tmp_path)

        if errores:
            return render(request, "core/formulario_124.html", {"errores": errores})

        pdf_salida = PDF_OUTPUT_DIR / "formulario_12_4_rellenado.pdf"
        rellenar_pdf_124(datos, PDF_ORIGINAL, pdf_salida)

        return FileResponse(
            open(pdf_salida, "rb"),
            content_type="application/pdf",
            as_attachment=True,
            filename="Formulario_12_4_rellenado.pdf",
        )

    return render(request, "core/formulario_124.html")

from pypdf import PdfReader
from django.http import HttpResponse

def debug_campos_pdf(request):
    reader = PdfReader(PDF_ORIGINAL)
    fields = reader.get_fields()

    texto = ""
    for name, field in fields.items():
        texto += f"NOMBRE: {name}\n"
        texto += f"DETALLE: {field}\n"
        texto += "-" * 50 + "\n"

    return HttpResponse(texto, content_type="text/plain")
