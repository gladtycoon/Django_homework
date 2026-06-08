from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Product


def home(request):
    return render(request, "home.html")


# def contacts(request):
#     return render(request, 'contacts.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Мы свяжемся с вами.")
    return render(request, "contacts.html")


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalog/products_list.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "catalog/product_detail.html", context)
