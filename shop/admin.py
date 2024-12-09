from django.contrib import admin
from shop.models import contact
from .models import Product,Orders,OrderUpdate
# Register your models here.
admin.site.register(contact)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)