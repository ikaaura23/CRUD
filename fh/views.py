from django.shortcuts import render

# Create your views here.
def indexfh(request):
    return render(request, 'fh-muka.html')