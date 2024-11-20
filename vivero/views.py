<<<<<<< HEAD
from django.shortcuts import render
from django import forms
from .models import Producto
from django.shortcuts import render, redirect

# Create your views here.
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'categoria', 'precio', 'cantidad']


#Vistas HU-1: Registro de Productos en el Inventario


def registrar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
=======
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vivero
from .forms import ViveroForm
from .forms import ProductoControlHongoForm, ProductoControlPlagaForm, ProductoControlFertilizanteForm
from .forms import LaborForm

def listar_viveros(request):
    viveros = Vivero.objects.all()
    return render(request, 'viveros/listar.html', {'viveros': viveros})

def crear_vivero(request):
    if request.method == 'POST':
        form = ViveroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_viveros')
    else:
        form = ViveroForm()
    return render(request, 'viveros/crear.html', {'form': form})

def editar_vivero(request, id):
    vivero = get_object_or_404(Vivero, id=id)
    if request.method == 'POST':
        form = ViveroForm(request.POST, instance=vivero)
        if form.is_valid():
            form.save()
            return redirect('listar_viveros')
    else:
        form = ViveroForm(instance=vivero)
    return render(request, 'viveros/editar.html', {'form': form})

def eliminar_vivero(request, id):
    vivero = get_object_or_404(Vivero, id=id)
    vivero.delete()
    return redirect('listar_viveros')








def registrar_producto_hongo(request):
    if request.method == 'POST':
        form = ProductoControlHongoForm(request.POST)
>>>>>>> origin/HU-2
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
<<<<<<< HEAD
        form = ProductoForm()
    return render(request, 'productos/registrar_producto.html', {'form': form})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar_productos.html', {'productos': productos})


def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listar_categorias.html', {'categorias': categorias})
=======
        form = ProductoControlHongoForm()
    return render(request, 'productos/registrar_hongo.html', {'form': form})

def registrar_producto_plaga(request):
    if request.method == 'POST':
        form = ProductoControlPlagaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoControlPlagaForm()
    return render(request, 'productos/registrar_plaga.html', {'form': form})

def registrar_producto_fertilizante(request):
    if request.method == 'POST':
        form = ProductoControlFertilizanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoControlFertilizanteForm()
    return render(request, 'productos/registrar_fertilizante.html', {'form': form})





def registrar_labor(request):
    if request.method == 'POST':
        form = LaborForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_labores')
    else:
        form = LaborForm()
    return render(request, 'labores/registrar.html', {'form': form})

def listar_labores(request):
    labores = Labor.objects.all()
    return render(request, 'labores/listar.html', {'labores': labores})
>>>>>>> origin/HU-2
