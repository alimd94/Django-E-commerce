from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", 'slug','weight','dimension','category','created_at','model_name','brand','image1','image2','image3',]


@admin.register(Product_Detalis)
class ProductDetalisAdmin(admin.ModelAdmin):
    list_display = ['product','color','price','has_Guaranty','quantity',]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name",'parent' ,'image',]

@admin.register(Promotions)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = ['product_Details','start_Date','end_Date','percentage',]

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ["key","value", "category"]