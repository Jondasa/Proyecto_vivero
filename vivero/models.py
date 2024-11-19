from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Productor(models.Model):
    documento_identidad = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Finca(models.Model):
    numero_catastro = models.CharField(max_length=50, unique=True)
    municipio = models.CharField(max_length=100)
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE, related_name='fincas')

    def __str__(self):
        return f"Finca {self.numero_catastro} - {self.municipio}"

class Vivero(models.Model):
    codigo = models.CharField(max_length=50)
    tipo_cultivo = models.CharField(max_length=100)
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, related_name='viveros')

    def __str__(self):
        return f"Vivero {self.codigo} - {self.tipo_cultivo}"

class ProductoControl(models.Model):
    registro_ica = models.CharField(max_length=50)
    nombre_producto = models.CharField(max_length=100)
    frecuencia_aplicacion = models.CharField(max_length=50)
    valor_producto = models.FloatField()

    class Meta:
        abstract = True

class ProductoControlHongo(ProductoControl):
    periodo_carencia = models.IntegerField()
    nombre_hongo = models.CharField(max_length=100)

class ProductoControlPlaga(ProductoControl):
    periodo_carencia = models.IntegerField()

class ProductoControlFertilizante(ProductoControl):
    fecha_ultima_aplicacion = models.DateField()

class Labor(models.Model):
    fecha = models.DateField()
    descripcion = models.TextField()
    vivero = models.ForeignKey(Vivero, on_delete=models.CASCADE, related_name='labores')

    # Relación genérica con la clase abstracta ProductoControl
    producto_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    producto_object_id = models.PositiveIntegerField()
    producto = GenericForeignKey('producto_content_type', 'producto_object_id')

    def __str__(self):
        return f"Labor {self.descripcion} - {self.fecha}"
    
#HU-1: Registro de Productos en el Inventario


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre    
    