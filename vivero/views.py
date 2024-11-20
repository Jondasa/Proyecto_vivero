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
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
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
