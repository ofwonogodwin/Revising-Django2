from django.contrib import admin

# Register your models here.
from .models import Item,Customer
admin.site.register(Item)
admin.site.register(Customer)