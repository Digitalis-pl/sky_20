from os import path
import json
from catalog.models import ContactInfo, Product, Category
import datetime

from django.shortcuts import render, get_object_or_404

# Create your views here.


def contacts(requests):
    data = {}
    if requests.method == 'POST':
        data['name'] = requests.POST.get('name')
        data['phone'] = requests.POST.get('phone')
        data['message'] = requests.POST.get('message')
        print(f'{data}')
        with open('data_folder/contactinfo_data.json', 'w', encoding="utf-8") as file:
            json.dump(data, file)
    contact = ContactInfo.objects.all()
    info = {'odj_info': contact}
    return render(requests, 'contacts.html', info)


def main_page(requests):
    if path.exists("product_data.json"):
        with open('product_data.json') as file:
            info = json.load(file)
            print(info[:6])
    return render(requests, 'main_page.html')


def product_page(requests):
    product = Product.objects.all()
    con = {'products': product}
    return render(requests, 'product_list.html', con)


def one_product(requests, name):
    prod = get_object_or_404(Product, name=name)
    context = {'product': prod}
    return render(requests, 'one_product_page.html', context)


def add_product_page(requests):
    prod_info = {}
    if requests.method == 'POST':
        prod_info['name'] = requests.POST.get('name')
        prod_info['price'] = requests.POST.get('price')
        category = requests.POST.get('category')
        cat_d = Category.objects.get(name=category).__dict__
        cat_id = cat_d['id']
        prod_info['img'] = requests.POST.get('img')
        prod_info['description'] = requests.POST.get('description')
        prod_info['created_at'] = datetime.datetime.now().strftime('%Y-%m-%d')
        prod_info['updated_at'] = datetime.datetime.now().strftime('%Y-%m-%d')
        Product.objects.create(**prod_info, category=Category.objects.get(pk=cat_id))
        prod_info['category'] = cat_id
        with open('data_folder/test.json', 'w', encoding='utf8') as f:
            json.dump(prod_info, f)
    category = Category.objects.all()
    cat = {'category': category}
    return render(requests, 'add_product.html', cat)


