from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (main_page, ProductView, OneProductView,
                           CreateContactView, ContactView,
                           CraeteProductView, BlogView,
                           BlogDetailView, BlogCreateView,
                           BlogUpdateView, BlogDeleteView)


app_name = CatalogConfig.name

urlpatterns = [
    path('', main_page),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('products/', ProductView.as_view(), name='product_page'),
    path('add_prod/', CraeteProductView.as_view(), name='add_prod'),
    path('our_product/<int:pk>', OneProductView.as_view(), name='one_product'),
    path('add_contact/', CreateContactView.as_view(), name='addcontact'),
    path('blog_main/', BlogView.as_view(), name='blog_main'),
    path('article/<int:pk>', BlogDetailView.as_view(), name='article'),
    path('create_article/', BlogCreateView.as_view(), name='create_article'),
    path('update_article/<int:pk>', BlogUpdateView.as_view(), name='update_view'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
]
