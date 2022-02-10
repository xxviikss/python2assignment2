from django.shortcuts import render, redirect

from scrap import topAccounts
from . models import Product
from . forms import ProductForm


# Create your views here.

def index(request):
    # products = Product.objects.all()

    # print(products)

    products = topAccounts()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()        

    context = {
        "products": products,
        
    }

    return render(request, 'chartapp/index.html', context)
