from django.contrib import admin

from customer.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'avatar']
    # readonly_fields = ["image_img", ]


admin.site.register(Customer, CustomerAdmin)
