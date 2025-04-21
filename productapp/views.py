from django.shortcuts import render
from .models import Product

# Create your views here.

def Home(request):
    return render(request, 'productapp/home.html')
def Add(request):
    context  = {
        'message':'',
    }
    if request.method == 'GET':
        return render(request,'productapp/add.html',context)
    if request.method == 'POST':
        prodname = request.POST.get('productname')
        prodprice = request.POST.get('productprice')
        ''' actual saving '''
        product = Product(name=prodname, price=prodprice)
        product.save()
        context['message'] = prodname + ' added successfully'
        return render(request, 'productapp/add.html',context)

def FetchAll(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'productapp/fetchall.html',context)