from django import forms
from .models import Categoria

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