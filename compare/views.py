from django.shortcuts import render,redirect
from django.views import View
from shop.models import Product
from django.views.generic import ListView
from .compare import Compare

class Index(View):
    def get(self,request):
        compare = Compare(request)
        template_name = "compare_index.html"
        context = {
            'compare':compare
            }
        return render(request,template_name,context,)

class AddCompare(View):
    def post(self,request,pk):
        compare = Compare(request)
        product = Product.objects.get(pk=pk)
        compare.add(product,request.POST.get('id'))
        return redirect("compare:index")

class DeleteCompare(View):
    def post(self,request,pk):
        compare = Compare(request)
        product = Product.objects.get(pk=pk)
        compare.remove(product)
        return redirect("compare:index")