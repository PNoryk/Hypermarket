from django.contrib import admin

# Register your models here.

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "picture", "image_img"]
    readonly_fields = ["image_img", ]
    
    # fields = ["picture", "image_img"]

    # class Meta:
    #     model = Product


# admin.site.register(Product, ProductAdmin)
