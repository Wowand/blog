from django.shortcuts import render, redirect
from collection.forms import ThingForm
from collection.models import Thing, Receipt, CartItem
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
    return render(request, 'things/thing_detail.html', {
        'thing': thing,
    })


def edit_thing(request, slug):
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
                             date_to=datetime.date(2015, 9, 10),
                             type="short")
    for item in result:
        receipt = Receipt(cartitems=item.cartitems,
                          date=item.date,
                          loyalty_id=item.loyalty_id,
                          receipt_id=item.receipt_id,
                          turnover=item.turnover,
                          )

        for cartItem in item.cartitems:
            cart = CartItem(name=cartItem)
            cart.save()
            receipt.cartitems.add(cart)
        receipt.save()
    return HttpResponse(json.dumps(result, default=date_handler), content_type="application/json")













