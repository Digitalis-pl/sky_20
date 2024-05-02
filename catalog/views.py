
import json

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
    return render(request, 'contacts.html')


def main_page(requests):
    return render(requests, 'main_page.html')
