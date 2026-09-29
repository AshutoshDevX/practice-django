from django.contrib import admin
from .models import Shop
# Register your models here.


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    search_fields = ('name','description')
    list_filter = ('name', 'price')
    ordering = ('name','price')