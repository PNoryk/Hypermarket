from django.contrib import admin

from products.models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image_img', 'created']


admin.site.register(ProductImage, ProductImageAdmin)
