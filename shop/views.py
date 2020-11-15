from django.shortcuts import render
from django.views import View
from shop.models import Product, Invoice, Order, Reviews, Category, Promotions, Favorites 

# Create your views here.
class Index(View):
    def get(self,request):
        template_name = "templates/index.html"
        context = {
            }
        return render(request,template_name,context,)

def product(request):
    template_name = "templates/product.html"
    return render(request,template_name)

def checkout(request):
    template_name = "templates/checkout.html"
    return render(request,template_name)

def store(request):
    template_name = "templates/store.html"
    return render(request,template_name)