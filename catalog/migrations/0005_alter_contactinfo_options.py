# Generated by Django 5.0.4 on 2024-05-04 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_contactinfo_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactinfo',
            options={'verbose_name': 'контактная информация'},
        ),
    ]