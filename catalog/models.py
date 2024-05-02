from django.db import models

# Create your models here.
null_options = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.ForeignKey('Category', on_delete=models.SET_NULL, **null_options)
    description = models.TextField(verbose_name='описание', **null_options)
    img = models.ImageField(upload_to='product/img')
    category = models.CharField(max_length=100)
    price = models.IntegerField(verbose_name='цена', **null_options)
    created_at = models.DateField(verbose_name='дата создания', **null_options)
    updated_at = models.DateField(verbose_name='дата последнего изменения', **null_options)

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
