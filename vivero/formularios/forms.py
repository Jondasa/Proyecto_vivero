from django import forms
from .models import Vivero, ProductoControlHongo, ProductoControlPlaga, ProductoControlFertilizante, Labor

class ViveroForm(forms.ModelForm):
    class Meta:
        model = Vivero
        fields = ['codigo', 'tipo_cultivo', 'finca']

class ProductoControlHongoForm(forms.ModelForm):
    class Meta:
        model = ProductoControlHongo
        fields = ['registro_ica', 'nombre_producto', 'frecuencia_aplicacion', 'valor_producto', 'periodo_carencia', 'nombre_hongo']

class ProductoControlPlagaForm(forms.ModelForm):
    class Meta:
        model = ProductoControlPlaga
        fields = ['registro_ica', 'nombre_producto', 'frecuencia_aplicacion', 'valor_producto', 'periodo_carencia']

class ProductoControlFertilizanteForm(forms.ModelForm):
    class Meta:
        model = ProductoControlFertilizante
        fields = ['registro_ica', 'nombre_producto', 'frecuencia_aplicacion', 'valor_producto', 'fecha_ultima_aplicacion']

class LaborForm(forms.ModelForm):
    class Meta:
        model = Labor
        fields = ['fecha', 'descripcion', 'vivero', 'producto_content_type', 'producto_object_id']
