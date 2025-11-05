from django.shortcuts import render
# importar una libreria para la autenticacion de las vistas
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def page_home(request):
    return render(request, "home/home.html")