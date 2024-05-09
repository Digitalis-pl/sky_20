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
                Category(name=category['fields']['name'],
                         description=category['fields']['description'])
            )

        Category.objects.bulk_create(category_for_create)

        cat = Category.objects.values_list('id', )
        num = []
        for el in cat:
            num.append(el[0])
        priv_num = max(num) - len(Command.read_info_category())
        x_list = []
        for x in Command.read_info_product():
            x_list.append(x['fields']['category'])
        prod = max(x_list)
        cicle_fst = max(num) - prod
        cicle_sec = cicle_fst / len(Command.read_info_category())
        last = cicle_sec * len(Command.read_info_category())

        for product in Command.read_info_product():
            my_num = product['fields']['category'] - priv_num
            product_for_create.append(
                Product(name=product['fields']['name'],
                        description=product['fields']['description'],
                        img=product['fields']['img'],
                        category=Category.objects.get(pk=round(my_num + last + priv_num)),
                        price=product['fields']['price'],
                        created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at']))

        Product.objects.bulk_create(product_for_create)
