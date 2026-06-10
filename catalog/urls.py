# from django.contrib import admin
from django.urls import include, path

from catalog.views import product_detail, products_list

from . import views

app_name = "catalog"

urlpatterns = [
    path("", products_list, name="products_list"),
    path("products/<int:pk>", product_detail, name="product_detail"),
]
