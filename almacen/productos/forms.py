from django import forms
from .models import Categoria, Proveedor

# crear un formulario personalizado para las Categorias
class CategoriaForm(forms.ModelForm):
    # ajuste al formulario generico
    class Meta:
        model = Categoria
        fields = ["nombre", "descripcion"]
        widgets = {
            "nombre": forms.TextInput(attrs={ "class": "form-control", "placeholder": "Nombre de la Categoria"}),
            "descripcion": forms.Textarea(attrs={ "class": "form-control", "placeholder": "Descripción de la Categoria", "rows": 3 })
        }
        
# crear un formulario personalizado para los proveedores
class ProveedorForm(forms.ModelForm):
    # ajustes al formulario
    class Meta:
        model = Proveedor
        fields = ["nombre", "telefono", "email", "direccion", "contacto"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del Proveedor"}),
            "telefono": forms.TextInput(attrs={"class": "form-control", "placeholder": "70544596", "type": "cel"}),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "alguien@example.com", "type": "email"}),
            "direccion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Direccion del proveedor", "rows": 3 }),
            "contacto": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del Contacto"}),
        }