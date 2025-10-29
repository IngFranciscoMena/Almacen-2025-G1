from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
# importar vistas genericas
from django.views.generic import CreateView
from .forms import RegistroUsuarioForm

# Create your views here.
class LoginViewPersonalizado(LoginView):
    template_name = "core/login.html"
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')

class LogoutViewPersonalizado(LogoutView):
    next_page = reverse_lazy('login')

class RegistroUsuarioCreateView(CreateView):
    template_name = "core/registro.html"
    form_class = RegistroUsuarioForm
    success_url = reverse_lazy('login')

    # sobreescribir el método form_valid
    def form_valid(self, form):
        # Guardar usuario con el método del formulario
        user = form.save()

        return super().form_valid(form)