from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (main_page, ProductView, OneProductView,
                           CreateContactView, ContactView,
                           CreateProductView, BlogView,
                           BlogDetailView, BlogCreateView,
                           BlogUpdateView, BlogDeleteView,
                           DeleteProduct, CreateVersionView,
                           VersionListView, VersionUpdateView,
                           activity_button, CategoryListView,
                           VersionDeleteView,)


app_name = CatalogConfig.name

urlpatterns = [
    path('', main_page),
    path('category/', CategoryListView.as_view(), name='category'),
    path('activity/<int:pk>', activity_button, name='activity'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('add_version/', CreateVersionView.as_view(), name='add_version'),
    path('versions/<int:pk>', VersionListView.as_view(), name='versions'),
    path('version_update/<int:pk>', VersionUpdateView.as_view(), name='update_version'),
    path('delete_version/<int:pk>', VersionDeleteView.as_view(), name='version_delete'),
    path('products/', ProductView.as_view(), name='product_page'),
    path('add_prod/', CreateProductView.as_view(), name='add_prod'),
    path('delete_product/<int:pk>', DeleteProduct.as_view(), name='delete_product'),
    path('our_product/<int:pk>', OneProductView.as_view(), name='one_product'),
    path('add_contact/', CreateContactView.as_view(), name='addcontact'),
    path('blog_main/', BlogView.as_view(), name='blog_main'),
    path('article/<int:pk>', BlogDetailView.as_view(), name='article'),
    path('create_article/', BlogCreateView.as_view(), name='create_article'),
    path('update_article/<int:pk>', BlogUpdateView.as_view(), name='update_view'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
]
