import csv


from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    data = []
    with open('data-398-2018-08-30.csv', newline='',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

content= [str(i) for i in 'data']
def pagi(request, ):
    page_number = int(request.GET.get("page",1))
    paginator = Paginator(content,10)
    page=paginator.get_page(page_number)

    context = {
         'bus_stations': index,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
