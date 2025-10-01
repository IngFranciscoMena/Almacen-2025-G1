# importar el método path
from django.urls import path
# importar las vistas
from .views import (
    ProductoListView
)

# nombre descriptivo para las url
app_name = "productos"

# crear el enrutamiento de las url
urlpatterns = [
    path('', ProductoListView.as_view(), name="producto-list"),
]