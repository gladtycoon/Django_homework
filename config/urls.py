from django.contrib import admin
from django.urls import path, re_path
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    re_path(r'^contacts/$', views.contacts, name='contacts'),
]