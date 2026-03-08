from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls")),   # conecta la app core
    path("admin/", admin.site.urls),
]
