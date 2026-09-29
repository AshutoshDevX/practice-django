from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='shop-home'),
    path('about/',views.products,name='shop-products'),
    path('renderHtml/',views.shop_list,name='shop_list')
]