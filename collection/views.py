from django.shortcuts import render, redirect
from  collection.forms import ThingForm
from collection.models import Thing
from pythonAPI import datawiz
import datetime
from django.http import HttpResponse
import json


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


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


def edit_thing(request, slyg):
    thing = Thing.objects.get(slug=slug)
    form_class = ThingForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            form.save()
            return redirect('thing_detail', slug=thing.slug)

    else:
        form = form_class(instance=thing)

    return render(request, 'things/edit_thing.html', {
        'thing': thing,
        'form': form,
    })


def get_receipts(request):
    dw = datawiz.DW()
    result = dw.get_receipts(
                             shops=[601],
                             weekday=6,
                             date_from=datetime.date(2015, 9, 2),
                             date_to=datetime.date(2015, 9, 29),
                             type="short")
    return HttpResponse(json.dumps(result, default=date_handler), content_type="application/json")





