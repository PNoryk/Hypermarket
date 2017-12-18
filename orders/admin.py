from django.contrib import admin
from orders.models import *


# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Status


# admin.site.register(Status, StatusAdmin)


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    readonly_fields = ['price_per_item', 'product_total_price']
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields if field.name != 'comments']
    readonly_fields = ['order_total_price']
    inlines = [ProductInOrderInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]
    readonly_fields = ['price_per_item', 'product_total_price']

    class Meta:
        model = ProductInOrder


# admin.site.register(ProductInOrder, ProductInOrderAdmin)
