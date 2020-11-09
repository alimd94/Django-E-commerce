from django.shortcuts import render

# Create your views here.
def index(request):
    template_name = "templates/index.html"
    return render(request,template_name)

def product(request):
    template_name = "templates/product.html"
    return render(request,template_name)

def checkout(request):
    template_name = "templates/checkout.html"
    return render(request,template_name)

def store(request):
    template_name = "templates/store.html"
    return render(request,template_name)