from django.urls import path
from .views import page_home

urlpatterns = [
    path('home/', page_home, name='home'),
]