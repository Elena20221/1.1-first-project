from typing import Dict, Any

from django.shortcuts import render, redirect
from phones.management.commands.import_phones import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    phones = Phone.objects.all()

    sort = request.GET.get('sort')  # параметр для режима сортировки

    if sort == 'name':
        phones = phones.order_by('name')
    elif sort == 'min_price':
        phones = phones.order_by('price')
    elif sort == 'max_price':
        phones = phones.order_by('-price')

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phone = Phone.objects.filter(slug=slug).first()

    context = {'phone': phone}


    return render(request, template,context)
