from django.shortcuts import render, get_object_or_404, redirect
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
    '''Get Query params order_by'''
    '''Get the key order_by otherwise set the value to name'''
    sortBy = request.GET.get('order_by','id')
    kword = request.POST.get('kword','')
    products = Product.objects.order_by(sortBy).filter(is_deleted=0)
    if kword:
        '''LIKE kword%'''
        ''' field<double underscore>i startswith/containswith/endswith/equal/greater'''
        products = products.filter(name__istartswith=kword)
    context = {
        'mgabaligya': products,
        'kword': kword
    }
    return render(request, 'productapp/fetchall.html',context)

def Update(request,uid):
    '''product/edit/<uid>'''
    ''' Get The row using the id passed'''
    product = get_object_or_404(Product,id=uid)
    if request.method == 'GET':
        context = {'baligya': product}
        return render(request,'productapp/edit.html',context)
    if request.method == 'POST':
        product.name = request.POST.get('productname')
        product.price = request.POST.get('productprice')
        product.save()
    return redirect('Fetch')

def HardDelete(request, uid):
    product = get_object_or_404(Product, id=uid)
    product.delete()
    return redirect('Fetch')

def SoftDelete(request, uid):
    product = get_object_or_404(Product, id=uid)
    product.is_deleted = 1
    product.save()
    return redirect('Fetch')
