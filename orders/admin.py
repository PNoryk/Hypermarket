from django.contrib import admin
from orders.models import *


# Register your models here.

class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields if field.name != 'comments']
    fields = []
    exclude = ['comments']

    class Meta:
        model = Order
        exclude = ['comments']


admin.site.register(Status)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder)
