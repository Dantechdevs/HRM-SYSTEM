from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

    
def manage(request):
    return render(request, 'manage.html', {})

    