from timeit import default_timer as timer
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.contrib.auth.models import Group


def shop_index(request):
    products = [
        ('Laptop', 1999),
        ('Desktop', 2999),
        ('Smartphone', 999)
    ]

    context = {
        "time_running": timer(),
        "products": products,
    }
    return render(request, 'shopapp/shop-index.html', context=context)


def groups_list(request):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)