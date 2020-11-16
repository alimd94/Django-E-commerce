from django.shortcuts import render
from django.views import View
from shop.models import Product, Invoice, Order, Reviews, Category, Promotions, Favorites
from django.views.generic import DetailView

# Create your views here.
class Index(View):
    def get(self,request):
        template_name = "index.html"
        context = {
            }
        return render(request,template_name,context,)

class ProductDetail(View):
    def get(self,request, pk):
        template_name = "product.html"
        product = Product.objects.get(pk=pk)
        context = {
            'product':product
            }
        return render(request,template_name,context,)

def product(request):
    template_name = "product.html"
    return render(request,template_name)

def checkout(request):
    template_name = "checkout.html"
    return render(request,template_name)

def store(request):
    template_name = "store.html"
    return render(request,template_name)