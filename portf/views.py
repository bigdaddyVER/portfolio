from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "portf/index.html")

def about(request):
    return render(request, "portf/about.html")

def works(request):
    return render(request, "portf/works.html")