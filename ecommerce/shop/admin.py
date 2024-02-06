from django.contrib import admin
from shop.models import Category,Product
from django.http import HttpResponse
admin.site.register(Category)
admin.site.register(Product)