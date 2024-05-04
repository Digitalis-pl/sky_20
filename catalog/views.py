from os import path
import json
from catalog.models import ContactInfo

from django.shortcuts import render

# Create your views here.


def contacts(request):
    data = {}
    if request.method == 'POST':
        data['name'] = request.POST.get('name')
        data['phone'] = request.POST.get('phone')
        data['message'] = request.POST.get('message')
        print(f'{data}')
        with open('user_data.json', 'w', encoding="utf-8") as file:
            json.dump(data, file)
    contact = ContactInfo.objects.all()
    info = {'odj_info': contact}
    return render(request, 'contacts.html', info)


def main_page(requests):
    if path.exists("category_data.json"):
        with open('product_data.json') as file:
            info = json.load(file)
            print(info[:6])
    return render(requests, 'main_page.html')
