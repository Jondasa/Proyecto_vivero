"""
URL configuration for utp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
<<<<<<< HEAD
urlpatterns = [
    path('admin/', admin.site.urls),
    #URL HU-1: Registro de Productos en el Inventario
    path('productos/registrar/', views.registrar_producto, name='registrar_producto'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('categorias/registrar/', views.registrar_categoria, name='registrar_categoria'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
=======

urlpatterns = [
    # Viveros
    path('viveros/', views.listar_viveros, name='listar_viveros'),
    path('viveros/crear/', views.crear_vivero, name='crear_vivero'),
    path('viveros/editar/<int:id>/', views.editar_vivero, name='editar_vivero'),
    path('viveros/eliminar/<int:id>/', views.eliminar_vivero, name='eliminar_vivero'),

    # Productos
    path('productos/hongo/registrar/', views.registrar_producto_hongo, name='registrar_producto_hongo'),
    path('productos/plaga/registrar/', views.registrar_producto_plaga, name='registrar_producto_plaga'),
    path('productos/fertilizante/registrar/', views.registrar_producto_fertilizante, name='registrar_producto_fertilizante'),

    # Labores
    path('labores/', views.listar_labores, name='listar_labores'),
    path('labores/registrar/', views.registrar_labor, name='registrar_labor'),
>>>>>>> origin/HU-2
]

