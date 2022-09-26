from django.shortcuts import render

# Create your views here.
def indexprofil(request):
    return render(request, 'profil-muka.html')
