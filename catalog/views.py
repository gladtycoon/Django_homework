from django.views.generic import DetailView, ListView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class HomeView(TemplateView):
    template_name = "home.html"


class ContactsView(TemplateView):
    template_name = "contacts.html"


class ProductDetailView(DetailView):
    model = Product


# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#         return HttpResponse(f"Спасибо, {name}! Мы свяжемся с вами.")
#     return render(request, "contacts.html")
#
#
# def products_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "catalog/products_list.html", context)
#
#
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, "catalog/product_detail.html", context)
