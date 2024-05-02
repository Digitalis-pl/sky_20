from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField
    img = models.ImageField(upload_to='product/img')
    category = models.CharField(max_length=100)
    price = models.IntegerField
    created_at = models.DateField
    updated_at = models.DateField
    manufactured_at = models.DateField(verbose_name='дата производства', blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.description} {self.category} {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
