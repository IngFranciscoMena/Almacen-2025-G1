from django.shortcuts import render
# importar vistas genericas
from django.views.generic import ListView, CreateView
# importar las clases
from .models import Producto, Categoria
# importar método reverse_lazy
from django.urls import reverse_lazy

# Create your views here.

# crear una clase generica para mostrar el listado de productos
class ProductoListView(ListView):
    
    # Indicar el modelo base
    model = Producto
    # Indicamos el template (plantilla)
    template_name = "producto/producto-list.html"
    # nombre del contexto del objetos
    context_object_name = "productos"
    
    
# crear una clase generica para mostrar el listado de categorias
class CategoriaListView(ListView):
    
    model = Categoria
    template_name = "categoria/categoria-list.html"
    context_object_name = "categorias"

class CategoriaCreateView(CreateView):
    
    model = Categoria
    fields = ["nombre", "descripcion"]
    template_name = "categoria/categoria-form.html"
    success_url = reverse_lazy("productos:categoria-list")
