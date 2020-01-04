
from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    cache_value = cache.get('cities')
    if not cache_value:
        cities = City.objects.all()
        cache.set('cities', cities, 60)

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""

    word = request.GET.get('term')
    cities = City.objects.filter(name__contains=word)

    results = []
    for city in cities:
        results.append(city.name)

    return JsonResponse(results, safe=False)
