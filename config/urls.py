# from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings
# from . import views
#
# urlpatterns = [
#     path("", views.home, name="home"),
#     path("contacts/", views.contacts, name="contacts"),
# ]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalog/", include("catalog.urls", namespace="catalog")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
