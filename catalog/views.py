from os import path
import json

import django

from catalog.models import ContactInfo, Product, Category, Blog, Version
import datetime

from django.urls import reverse_lazy, reverse

from impinfo import user

from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm

from django.core.mail import send_mail

from django.template.loader import render_to_string

from pytils.translit import slugify

# Create your views here.


class VersionListView(ListView):
    model = Version

    def get_queryset(self):
        queryset = super().get_queryset()

        prod_pk = self.request.GET
        prod = Product.objects.get(pk=prod_pk['id'])
        queryset = queryset.filter(product=prod).order_by('id')
        return queryset


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self):
        return f'{reverse('catalog:versions', kwargs={'pk': self.object.product.pk})}?id={self.object.product.pk}'


class VersionDeleteView(DeleteView):
    model = Version

    def get_success_url(self):
        return f'{reverse('catalog:versions', kwargs={'pk': self.object.product.pk})}?id={self.object.product.pk}'


class CreateContactView(CreateView):
    model = ContactInfo
    fields = ('name', 'phone', 'message',)
    success_url = reverse_lazy('catalog:contacts')


class ContactView(ListView):
    model = ContactInfo


class CategoryListView(ListView):
    model = Category

#def contacts(requests):
#    data = {}
#    if requests.method == 'POST':
#        data['name'] = requests.POST.get('name')
#        data['phone'] = requests.POST.get('phone')
#        data['message'] = requests.POST.get('message')
#        print(f'{data}')
#        with open('data_folder/contactinfo_data.json', 'w', encoding="utf-8") as file:
#            json.dump(data, file)
#    contact = ContactInfo.objects.all()
#    info = {'odj_info': contact}
#    return render(requests, 'contacts.html', info)


def main_page(requests):
    if path.exists("product_data.json"):
        with open('product_data.json') as file:
            info = json.load(file)
            print(info[:6])
    return render(requests, 'catalog/main_page.html')


#def product_page(requests):
#    product = Product.objects.all()
#    con = {'products': product}
#    return render(requests, 'product_detail.html', con)

class ProductView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        for prod in products:
            versions = Version.objects.filter(product=prod)
            active_version = versions.filter(version_sign=True)
            if active_version:
                prod.active_version = active_version.last().version_name
            else:
                prod.active_version = 'Нет последней версии'
        context['object_list'] = products
        return context


class OneProductView(DetailView):
    model = Product




#def one_product(requests, pk):
#    prod = get_object_or_404(Product, pk=pk)
#    context = {'product': prod}
#    return render(requests, 'product_detail.html', context)


class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:add_prod')


class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_page')


class CreateVersionView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:add_version')


#def add_product_page(requests):
#    prod_info = {}
#    if requests.method == 'POST':
#        prod_info['name'] = requests.POST.get('name')
#        prod_info['price'] = requests.POST.get('price')
#        category = requests.POST.get('category')
#        cat_d = Category.objects.get(name=category).__dict__
#        cat_id = cat_d['id']
#        prod_info['img'] = requests.POST.get('img')
#        prod_info['description'] = requests.POST.get('description')
#        prod_info['created_at'] = datetime.datetime.now().strftime('%Y-%m-%d')
#        prod_info['updated_at'] = datetime.datetime.now().strftime('%Y-%m-%d')
#        Product.objects.create(**prod_info, category=Category.objects.get(pk=cat_id))
#        prod_info['category'] = cat_id
#        with open('data_folder/test.json', 'w', encoding='utf8') as f:
#            json.dump(prod_info, f)
#    category = Category.objects.all()
#    cat = {'category': category}
#    return render(requests, 'catalog/add_product.html', cat)


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'photo', 'created_at', 'published', 'view_counter',)
    success_url = reverse_lazy('catalog:blog_main')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
            return super().form_valid(form)


class BlogView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published=True)
        for article in Blog.objects.all():
            if article.view_counter == 100:
                send_mail(
                    "Поздравления!",
                    "Статья набрала 100 просмотров!",
                    'zhora.karsakov@yandex.ru',
                    ["someone@mail.ru"],
                    fail_silently=False,
                )
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'photo', 'created_at', 'published', 'view_counter',)

    def get_success_url(self):
        return reverse('catalog:article', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_main')


def activity_button(request, pk):
    flags = []
    all_vers = Version.objects.all()
    for vers in all_vers:
        vers.error_message = None
        vers.save()
        flags.append(vers.version_sign)
    obj = get_object_or_404(Version, pk=pk)
    prod_name = obj.product
    prod_pk = Product.objects.get(name=prod_name.name)
    if obj.version_sign:
        obj.version_sign = False
    else:
        if True in flags:
            obj.error_message = 'может быть только одна активная версия'
            obj.save()

            return redirect(f'{reverse('catalog:versions', kwargs={'pk': prod_pk.id})}?id={prod_pk.id}')
        else:
            obj.version_sign = True

    obj.save()

    return redirect(f'{reverse('catalog:versions', kwargs={'pk': prod_pk.id})}?id={prod_pk.id}')
