from django.contrib import admin
from . models import Product, Heading, Category, Subcategory
# Register your models here.

@admin.register(Product)
class Admin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'price', 'img', 'que','subcategory',]
    
@admin.register(Category)
class Admin(admin.ModelAdmin):
    list_display = ["category_name"]

@admin.register(Subcategory)
class Admin(admin.ModelAdmin):
    list_display = ['sub_category_name']

@admin.register(Heading)
class Admin(admin.ModelAdmin):
    list_display = ['heading_name']