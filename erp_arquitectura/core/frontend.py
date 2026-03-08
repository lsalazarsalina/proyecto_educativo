from __future__ import annotations
from pathlib import Path
from django.shortcuts import render

def index_frontend(request):
    return render(request, "frontend/index.html")