from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader

from .models import Product

# Create your views here.
def index(request):
    products_list=Product.objects.order_by('-title')[:7]
    template=loader.get_template('products/index.html')
    context={
        'product_list':products_list
    }
    output = ', '.join([p.title for p in products_list])
    return HttpResponse(output)

    # return HttpResponse(template,render(context,request))

    # return HttpResponse("<h1>Hello Product index view</h1>")
