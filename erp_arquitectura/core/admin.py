from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cliente, Predio, Proyecto

admin.site.register(Cliente)
admin.site.register(Predio)
admin.site.register(Proyecto)