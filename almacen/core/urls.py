from django.urls import path
from .views import LoginViewPersonalizado, LogoutViewPersonalizado

urlpatterns = [
    path('login/', LoginViewPersonalizado.as_view(), name='login'),
    path('logout/', LogoutViewPersonalizado.as_view(), name='logout'),
]
