from django.conf import settings
from shop.models import Product

class Compare():

    def __init__(self, request):
        self.session = request.session
        compare = self.session.get(settings.COMPARE_SESSION_ID)
        if not compare:
            compare = self.session[settings.COMPARE_SESSION_ID] = {}
        self.compare = compare
    

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.compare:
            self.compare[product_id]=product_id
        self.save()


    def save(self):
        self.session[settings.COMPARE_SESSION_ID] = self.compare
        self.session.modified = True
        

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.compare:
            del self.compare[product_id]
            self.save()
    
    def __iter__(self):
        product_ids = self.compare.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.compare[str(product.id)]['product'] = product

        for item in self.compare.values():
            yield item
    
    def __len__(self):
        return sum(int(item['quantity']) for item in self.cart.values())

    # def get_total_price(self):
    #     return sum(Decimal(item['price']) * Decimal(item['quantity']) for item in self.cart.values())

    def clear(self):
        del self.session[settings.COMPARE_SESSION_ID]
        self.session.modified = True