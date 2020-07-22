from django.contrib import admin
from .models import sub_categorie,categorie,Products
from django.db import connection
from django.shortcuts import render,redirect
from . import views
# Register your models here.
admin.site.site_header = 'MyShop Administration'

class ProductsAdmin(admin.ModelAdmin):

    change_form_template = 'admin/categories.html'


admin.site.register(sub_categorie)
admin.site.register(categorie)
admin.site.register(Products,ProductsAdmin)