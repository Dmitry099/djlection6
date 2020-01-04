from django import forms
from django.core.cache import cache

from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    city_from = forms.CharField(widget=AjaxInputWidget(url='api/city_ajax',
                                                       attrs={'class': 'inline right-margin'}),
                                label='Город отправления')
    value = cache.get('cities')
    if value:
        city_to = forms.ModelChoiceField(queryset=value, label='Город прибытия')
    else:
        city_to = forms.ModelChoiceField(queryset=City.objects.all(), label='Город прибытия')
    time = forms.DateField(widget=forms.SelectDateWidget, label='Дата')
