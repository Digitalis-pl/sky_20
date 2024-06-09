from django.db import models
from users.models import User

# Create your models here.
null_options = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название товара', **null_options)
    description = models.TextField(verbose_name='описание', **null_options)
    img = models.ImageField(upload_to='product/img')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, **null_options)
    price = models.IntegerField(verbose_name='цена', **null_options)
    created_at = models.DateField(verbose_name='дата создания', **null_options)
    updated_at = models.DateField(verbose_name='дата последнего изменения', **null_options)

    product_owner = models.ForeignKey(User, verbose_name='product_owner', on_delete=models.SET_NULL, **null_options)

    def __str__(self):
        return f'{self.name} {self.description} {self.category} {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(verbose_name='описание', **null_options)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class ContactInfo(models.Model):
    name = models.CharField(max_length=60, verbose_name='имя пользователя', **null_options)
    phone = models.CharField(max_length=20, verbose_name='телефон', **null_options)
    message = models.TextField(verbose_name='текст', **null_options)

    def __str__(self):
        return f'{self.name} {self.phone} {self.message}'

    class Meta:
        verbose_name = 'контактная информация'


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.CharField(max_length=200, verbose_name='Ссылка', **null_options)
    content = models.TextField(verbose_name='текст', **null_options)
    photo = models.ImageField(upload_to='articles/photo')
    created_at = models.DateField(verbose_name='дата создания', **null_options)
    published = models.BooleanField(default=True, verbose_name='опубликовано')
    view_counter = models.IntegerField(default=0, verbose_name='количество просмотров')

    article_owner = models.ForeignKey(User, verbose_name='product_owner', on_delete=models.SET_NULL, **null_options)

    def __str__(self):
        return f'{self.title} {self.slug} {self.content} {self.photo} {self.created_at} {self.published} {self.view_counter}'

    class Meta:
        verbose_name = 'Блог'


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, **null_options,  related_name='products')
    version_counter = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    version_sign = models.BooleanField(default=True, verbose_name='признак версии')
    error_message = models.CharField(max_length=38, verbose_name='может быть только одна активная версия', **null_options)
