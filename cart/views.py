from django.shortcuts import render,redirect,reverse
from django.views import View
from shop.models import Product
from django.views.generic import ListView
from .cart import Cart

class Index(View):
    def get(self,request):
        cart = Cart(request)
        template_name = "cart_index.html"
        context = {
            'cart':cart
            }
        return render(request,template_name,context,)

class AddCart(View):
    def post(self,request,pk):
        cart = Cart(request)
        product = Product.objects.get(pk=pk)
        cart.add(product,1,1000)
        return redirect("cart:index")

class DeleteCart(View):
    def post(self,request,pk):
        cart = Cart(request)
        product = Product.objects.get(pk=pk)
        cart.remove(product)
        return redirect("cart:index")