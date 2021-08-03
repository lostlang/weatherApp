from django.shortcuts import render
from django.utils import timezone

from . import apps, models

# Create your views here.


def index(request):
    api = apps.MeteoApi()
    content = api.get_data()
    log = models.Log(
        date=timezone.now().date(),
        time=timezone.now().time()
    )
    log.save()
    return render(request, 'base.html', content)
