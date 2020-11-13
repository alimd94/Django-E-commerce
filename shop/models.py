from django.db import models
from mptt import models as mpttmodels
from django.utils.text import slugify

# Create your models here.
class Category(mpttmodels.MPTTModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/category/%Name")
    parent = mpttmodels.TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name
    
class Property(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.key + ":" + self.value


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    weight = models.IntegerField()
    dimension = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default="No Category")
    created_at = models.DateTimeField(auto_now_add=True)
    model_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to="images/product/%ID")
    image2 = models.ImageField(upload_to="images/product/%Id", null=True, blank=True)
    image3 = models.ImageField(upload_to="images/product/%pk", null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Product_Detalis(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    color = models.CharField(max_length=100)
    price = models.IntegerField()
    has_Guaranty = models.BooleanField()
    quantity = models.IntegerField()
    property = models.ManyToManyField(Property)
    
    def __str__(self):
        return self.product.name + " Details"

class Promotions(models.Model):
    product_Details = models.ForeignKey(Product_Detalis, on_delete=models.CASCADE,)
    start_Date = models.DateTimeField()
    end_Date = models.DateTimeField()
    percentage = models.IntegerField()

    def __str__(self):
        return self.product_Details.product.name + " OFF! -->" + str(self.percentage)

# class User():
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email
#     phone_Number
#     password
#     addresses
#     created_at
#     updated_at
#     is_active

# class Reviews(models.Model):
#     user
#     title
#     body
#     created_at
#     product
#     rating

# class Favorites(models.Model):
#     user
#     product


# class Order(models.Model):
#     product_Details
#     user
#     address
#     quantity
#     price
#     created_at
#     status
#     description
#  address
