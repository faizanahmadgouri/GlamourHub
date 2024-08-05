
from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product

def index(request):
    products=Product.objects.all()
    print(products)
    context={
        'Products':products
    }
    return render(request,'index.html',context)