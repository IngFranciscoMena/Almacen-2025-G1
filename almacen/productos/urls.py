# importar el método path
from django.urls import path
# importar las vistas
from .views import (
    # Producto
    ProductoListView,
    # Categoria
    CategoriaListView,
    CategoriaCreateView,
    
)

# nombre descriptivo para las url
app_name = "productos"

# crear el enrutamiento de las url
urlpatterns = [
    path('', ProductoListView.as_view(), name="producto-list"),
    path('categoria/', CategoriaListView.as_view(), name="categoria-list"),
    path('categoria/nuevo', CategoriaCreateView.as_view(), name="categoria-create")
]