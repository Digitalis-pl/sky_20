from django.contrib import admin
from catalog.models import Product, Category, ContactInfo, Blog
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'is_published')
    list_filter = ('category',)
    search_fields = ('description', 'name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('description', 'name')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'message')
    list_filter = ('name', 'phone')
    search_fields = ('phone', 'name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'article_owner', 'published', 'slug')
    list_filter = ('title', 'article_owner', 'published')
    search_fields = ('article_owner', 'title')
