from django.db import models
from mptt import models as mpttmodels
from django.utils.text import slugify
import os
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import time 
  

class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    phone_Number = models.CharField(max_length=11)
    addresses = models.TextField()
    updated_at =  models.DateField(auto_now=True)


def get_upload_path(instance, filename):
    if hasattr(instance,'category'):
        tmp = os.path.join('images', str(instance.category),str(instance.name),filename)
        return tmp
    elif hasattr(instance,'parent'):
        tmp = os.path.join('images','category',filename)
        return tmp
    else:
        tmp = os.path.join('images','brand',filename)
        return tmp

# Create your models here.
class Category(mpttmodels.MPTTModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_upload_path)
    parent = mpttmodels.TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_upload_path)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_DEFAULT, default="No Brand")
    specification= models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    long_description = models.TextField()
    short_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default="No Category")
    number_of_sold = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    image1 = models.ImageField(upload_to=get_upload_path)
    image2 = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    image3 = models.ImageField(upload_to=get_upload_path, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Promotions(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    start_Date = models.DateTimeField()
    end_Date = models.DateTimeField()
    percentage = models.IntegerField()

    def __str__(self):
        return self.product.product.name + " OFF! -->" + str(self.percentage)


class Reviews(models.Model):

    class RT(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices = RT.choices)

class Favorites(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



class Order(models.Model):

    class StatusChoice(models.TextChoices):
        PENDING = 'P', 'Pending'
        SUCCESFUL = 'S', 'Succesful'
        CANCELED = 'C', 'Canceled'
        
    product = models.ManyToManyField(Product,through='OrderItems')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_quantity = models.IntegerField()
    total_cost = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateField(auto_now=True)
    status = models.CharField(max_length=1,choices=StatusChoice.choices, default=StatusChoice.PENDING)
    description = models.TextField()


class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_cost = models.DecimalField(decimal_places=2, max_digits=10)
    total_product_cost = models.DecimalField(decimal_places=2, max_digits=10)

    def save(self, *args, **kwargs):
        self.unit_cost = self.quantity * self.unit_cost
        super(OrderItems, self).save(*args, **kwargs)
