from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", 'slug','category','created_at','image1','image2','image3','description','price']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name",'parent' ,'image',]

@admin.register(Promotions)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = ['product','start_Date','end_Date','percentage',]
