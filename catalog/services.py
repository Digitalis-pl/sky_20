from django.core.cache import cache

from config.settings import CACHE_ENABLED
from catalog.models import Product


def get_prod_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'product_list'
    products = cache.get(key)
    if products is not None:
        return products
    Product.objects.all()
    cache.set(key, products)
    return products
