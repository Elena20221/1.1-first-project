from django.urls import path

from .views import index, bus_stations,pagi

urlpatterns = [
    path('', index, name='index'),
    path('bus_stations/', bus_stations, name='bus_stations'),
    path('pagi/',pagi,name='pagi'),
]
