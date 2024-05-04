import json
from django.core.management import BaseCommand
from catalog.models import Category, Product
from os import path


class Command(BaseCommand):

    @staticmethod
    def read_info_category():
        if path.exists("data_folder/category_data.json"):
            with open('data_folder/category_data.json', encoding='utf8') as file:
                data = json.load(file)
            return data

    @staticmethod
    def read_info_product():
        if path.exists("data_folder/product_data.json"):
            with open('data_folder/product_data.json', encoding='utf8') as file:
                return json.load(file)

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.read_info_category():
            category_for_create.append(
                Category(name=category['fields']['name'], description=category['fields']['description'])
            )

        Category.objects.bulk_create(category_for_create)

        cat = Category.objects.values_list('id', )
        num = []
        for el in cat:
            num.append(el[0])

        for product in Command.read_info_product():
            my_num = product["fields"]['category'] / product["fields"]['category']-len(Command.read_info_category())
            category_for_create.append(
                Product(name=product['fields']['name'],
                        description=product['fields']['description'],
                        img=product['fields']['img'],
                        category=Category.objects.get(pk=my_num + max(num)),
                        price=product['fields']['price'], created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at'])
            )

        Product.objects.bulk_create(product_for_create)
