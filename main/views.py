from django.shortcuts import render, redirect
from main.forms import ECommerceForm
from main.models import ECommerce
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    order_entries = ECommerce.objects.all()
    context = {
        'app_name' : 'Gopedia',
        'nama' : 'Ragnall Muhammad Al Fath',
        'npm' : '2306210550',
        'kelas' : 'PBP C',
        'name' : '24/25 Away Kit',
        'price': '1500000',
        'description': 'Manchester United Away Kit for the 24/25 Season',
        'order_entries': order_entries
    }

    return render(request, "main.html", context)

def create_order(request):
    form = ECommerceForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_order.html", context)

def show_xml(request):
    data = ECommerce.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ECommerce.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ECommerce.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ECommerce.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")