
from shop.models import Category
from cart.cart import Cart

def get_cart(request):
    cart = Cart(request)
    context = {
            'cart':cart
            }
    return context

def get_categories(request):
    categories = Category.objects.all()
    return {
        'categories': categories
    }
