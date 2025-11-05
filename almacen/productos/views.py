from django.shortcuts import render
# importar vistas genericas
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# importar las clases
from .models import Producto, Categoria, Proveedor
# importar método reverse_lazy
from django.urls import reverse_lazy
# importar los formularios personalizados
from .forms import CategoriaForm, ProveedorForm, ProductoForm
# importar una libreria para la autenticacion de las vistas
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# crear una clase generica para mostrar el listado de productos

class ProductoListView(LoginRequiredMixin, ListView):
    
    # Indicar el modelo base
    model = Producto
    # Indicamos el template (plantilla)
    template_name = "producto/producto-list.html"
    # nombre del contexto del objetos
    context_object_name = "productos"
    
class ProductoCreateView(LoginRequiredMixin, CreateView):

    model = Producto
    form_class = ProductoForm
    template_name = "producto/producto-form.html"
    success_url = reverse_lazy("productos:producto-list")

# crear una nueva vista generica para editar un producto
class ProductoUpdateView(LoginRequiredMixin, UpdateView):

    model = Producto
    form_class = ProductoForm
    template_name = "producto/producto-form.html"
    success_url = reverse_lazy("productos:producto-list")

class ProductoDetailView(LoginRequiredMixin, DetailView):
    
    model = Producto
    template_name = "producto/producto-detail.html"
    context_object_name = "producto"

class ProductoDeleteView(LoginRequiredMixin, DeleteView):

    model = Producto
    template_name = "producto/producto-confirm.html"
    success_url = reverse_lazy("productos:producto-list")

    # polimorfismo
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = f"Eliminar producto: {self.object.nombre}"
        return context

    
# crear una clase generica para mostrar el listado de categorias
class CategoriaListView(LoginRequiredMixin, ListView):
    
    model = Categoria
    template_name = "categoria/categoria-list.html"
    context_object_name = "categorias"

# crear una clase generica para guardar una nueva categoria
class CategoriaCreateView(LoginRequiredMixin, CreateView):
    
    model = Categoria
    form_class = CategoriaForm
    template_name = "categoria/categoria-form.html"
    success_url = reverse_lazy("productos:categoria-list")
    
    
# crear una clase generica para mostrar el listado de proveedor
class ProveedorListView(LoginRequiredMixin, ListView):
    
    model = Proveedor
    template_name = "proveedor/proveedor-list.html"
    context_object_name = "proveedores"

# crear una clase generica para guardar un nuevo proveedor
class ProveedorCreateView(LoginRequiredMixin, CreateView):
    
    model = Proveedor
    form_class = ProveedorForm
    template_name = "proveedor/proveedor-form.html"
    success_url = reverse_lazy("productos:proveedor-list")
