from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from ecommerce import settings
from django.contrib.auth.admin import UserAdmin
from django_mptt_admin.admin import DjangoMpttAdmin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
import csv
from django.http import HttpResponse

# Register your models here.
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_display = ["name", 'slug','category','brand','price','created_at','quantity','number_of_sold','view_detail']
    icon_name = 'shop'
    actions = ["export_as_csv"]

    def view_detail(self, obj):
        url = reverse('shop:detail', args={obj.id})
        return format_html('<a href="{}"> Details </a>', url)

    view_detail.short_description = "Details"


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ["name",'parent' ,'image',]

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name" ,'image',]

admin.site.register(User, UserAdmin)
# @admin.register(User,UserAdmin)
# class Useradmin(admin.ModelAdmin):
#     list_display = ["username",]


class CategoryAdmin(DjangoMpttAdmin):
    list_display = ["name",'parent' ,'image',]

admin.site.register(Category, CategoryAdmin)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["total_cost" ,'user',]
    list_filter = (
        ('created_at', DateRangeFilter), ('updated_at', DateTimeRangeFilter),
    )

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ["key","value", "category"]