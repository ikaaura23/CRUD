from django.shortcuts import render

# Create your views here.
def indexfk(request):
    return render(request, 'fk-muka.html')