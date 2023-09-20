from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import ProductForm
from main.models import Item
from django.http import HttpResponse
from django.core import serializers


def show_main(request):
    items = Item.objects.all()
    count= Item.objects.all().count()


    context = {
        'app_name': 'Inventory Management',
        'name': 'Tiva Adhisti Nafira Putri',
        'class': 'PBP KI',
        'items': items,
        'items_count': count,
    
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Retrieving Data Based on ID in XML and JSON Formats
def show_xml_by_id(request, id):
    # store the query result of data with a specific ID from the Product model
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    # store the query result of data with a specific ID from the Product model
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")