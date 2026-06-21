from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from catalog.views import ContactsView, HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),  # ← главная без префикса
    path(
        "contacts/", ContactsView.as_view(), name="contacts"
    ),  # ← контакты без префикса
    path("admin/", admin.site.urls),
    path("catalog/", include("catalog.urls", namespace="catalog")),
    path("blog/", include("blog.urls", namespace="blog")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
