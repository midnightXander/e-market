from django.contrib import admin
from .models import Category,Item,Item_in_bag,Order_details

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Item_in_bag)
admin.site.register(Order_details)