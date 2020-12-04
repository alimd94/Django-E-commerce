from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", 'slug','category','brand','price','short_description','long_description','created_at','image1','image2','image3']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name",'parent' ,'image',]

@admin.register(Brand)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name" ,'image',]


