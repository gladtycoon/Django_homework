from django.core.cache import cache

from catalog.models import Product
from config.settings import CASHE_ENABLED


def get_products_from_cache():
    """Получает список продуктов из кэша. Если кэш пустой - получает данные из БД"""
    if not CASHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products
