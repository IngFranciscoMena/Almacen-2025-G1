from django.shortcuts import render
# importar vistas genericas
from django.views.generic import ListView
# importar las clases
from .models import Producto

# Create your views here.

# crear una clase generica para mostrar el listado de productos
class ProductoListView(ListView):
    
    # Indicar el modelo base
    model = Producto
    # Indicamos el template (plantilla)
    template_name = "producto/producto-list.html"
    # nombre del contexto del objetos
    context_object_name = "productos"

