from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import main_page, contacts, product_page, add_product_page, one_product


app_name = CatalogConfig.name

urlpatterns = [
    path('', main_page),
    path('contacts/', contacts),
    path('products/', product_page),
    path('add_prod/', add_product_page, name='add_prod'),
    path('our_product/<str:name>', one_product),
]
