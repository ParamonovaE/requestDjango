import csv

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


CONTENT = BUS_STATION_CSV


def bus_stations(request):
    with open(CONTENT, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations = list(reader)  # Преобразование данных в список словарей

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(stations, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page.object_list,  # Список станций на текущей странице
        'page': page,                      # Текущая страница
    }
    return render(request, 'stations/index.html', context)
