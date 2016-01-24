from django.shortcuts import render
from collection.models import Thing
from pythonAPI import datawiz
import datetime
from django.http import HttpResponse
import json


def index(request):
    number = 6
    things = Thing.objects.all()
    return render(request, 'index.html', {
        'number': number,
        'things': things,
    })


def things_details(request, slug):
    thing = Thing.objects.get(slug=slug)
    return render(request, 'things/things_detail.html', {
        'thing': thing,
    })


def get_receipts(request):
    dw = datawiz.DW()
    result = dw.get_receipts(categories=[50599, 50600],
                             shops=[601, 641],
                             date_from=datetime.date(2015, 12, 28),
                             date_to=datetime.date(2016, 1, 20),
                             type="short")
    return HttpResponse(json.dumps(result))


