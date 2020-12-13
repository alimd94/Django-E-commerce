from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from shop.models import Product, Order, Reviews, Category, Promotions, Favorites, Brand
from django.views.generic import DetailView

# Create your views here.
#              #            1-parent categories Category.objects.filter(parent__isnull=True)
#              #            2-new product (by category) Product.objects.filter(category=Category.objects.get(id=6)).order_by('created_at')[:10]
#              #            3-hot deal     --> image                      
#              #            4-top selling (by category)
#              #            5-top brand distinct("brand")
#                           6-top best selling product prod = Product.objects.annotate(num_orders=Count('order')).order_by('num_orders')[:10]
#
class Index(View): 
    def get(self,request):
        if request.GET.get('id'):
            id = request.GET.get('id')
            _product = Product.objects.get(pk=id)
            product=dict()
            product["name"] = _product.name
            product["price"] = _product.price
            product["short_description"] = _product.short_description
            product["image"] = _product.image1.url
            return JsonResponse(product)
        categories = Category.objects.filter(parent__isnull=True)
        newProducts = {}
        topSellings = {}
        for category in categories:
          newProducts[category.name] = Product.objects.filter(category=category.id).order_by('created_at')[:5]
          topSellings[category.name] = Product.objects.filter(category=category.id).order_by('number_of_sold')[:5]
        topBrand = Brand.objects.all().order_by('product__number_of_sold')[:5]
        
        template_name = "index.html"
        context = {
            'topBrands': topBrand,
            'newProducts': newProducts,
            'categories': categories,
            'topSellings': topSellings,
            }
        return render(request,template_name,context,)
    



class ProductDetail(View):
    def get(self,request, pk):
        template_name = "product.html"
        product = Product.objects.get(pk=pk)
        categories = Category.objects.get(pk=product.category.id).get_family()
        relatedP = Product.objects.filter(category=product.category).exclude(pk=pk)[:5]
        context = {
            'product':product,
            'categories':categories,
            'relatedP': relatedP
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