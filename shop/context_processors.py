
from shop.models import Category

def get_context(request):
    categories = Category.objects.all()
    return {
        'categories': categories
    }
