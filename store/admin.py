from django.contrib import admin
from .models import *
admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Platform)
admin.site.register(Publisher)
admin.site.register(Tag)
admin.site.register(Discount)
admin.site.register(DLC)
admin.site.register(Order)
admin.site.register(OrderItem)