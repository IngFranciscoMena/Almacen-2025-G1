from django.urls import path
from .views import LoginViewPersonalizado, LogoutViewPersonalizado, RegistroUsuarioCreateView

urlpatterns = [
    path('login/', LoginViewPersonalizado.as_view(), name='login'),
    path('logout/', LogoutViewPersonalizado.as_view(), name='logout'),
    path('registro/', RegistroUsuarioCreateView.as_view(), name='registro')
]
