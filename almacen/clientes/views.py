from django.shortcuts import render

# Create your views here.
def page_home(request):
    return render(request, "home/home.html")