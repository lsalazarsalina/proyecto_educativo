from django.db import models

# Create your models here.
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    rut = models.CharField(max_length=12, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre


class Predio(models.Model):
    direccion = models.CharField(max_length=250)
    comuna = models.CharField(max_length=100)
    rol = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.direccion} - {self.comuna}"


class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)
    superficie = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)



    def __str__(self):
        return self.nombre


class Expediente20898(models.Model):
    ESTADO_CHOICES = [
        ("borrador", "Borrador"),
        ("ingresado", "Ingresado DOM"),
        ("observado", "Con observaciones"),
        ("aprobado", "Aprobado"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True, blank=True)

    destino = models.CharField(max_length=100, default="Habitacional")
    superficie_existente = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    superficie_regularizar = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    anio_construccion = models.IntegerField(null=True, blank=True)

    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default="borrador")
    fecha_ingreso = models.DateField(null=True, blank=True)

    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Expediente 20.898 - {self.predio}"