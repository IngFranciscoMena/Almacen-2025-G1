from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class LoginViewPersonalizado(LoginView):
    template_name = "core/login.html"
    redirect_authenticated_user = True

class LogoutViewPersonalizado(LogoutView):
    next_page = reverse_lazy('login')
