from django.contrib import admin

from products.models import *


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


# @admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image_img', 'is_main', 'created']
    # list_display = [field.name for field in ProductImage._meta.fields]
    # fields = (('product', 'created'), 'is_main')
    # exclude = ['created']


admin.site.register(ProductImage, ProductImageAdmin)
