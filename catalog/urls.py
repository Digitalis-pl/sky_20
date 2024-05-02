from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import main_page, contacts


app_name = CatalogConfig.name

urlpatterns = [
    path('', main_page),
    path('contacts/', contacts),
]
