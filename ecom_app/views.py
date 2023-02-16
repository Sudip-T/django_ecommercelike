from django.shortcuts import render
from ecom_app.models import *
from django.http import JsonResponse


def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'ecom_app/store.html', context)

def cart(request):
	context = {}
	return render(request, 'ecom_app/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'ecom_app/checkout.html', context)

def search(request):
	search = request.GET['search']
	data = Product.objects.filter(title_icontains=search).order_by('-id')
	return render(request, 'ecom_app/search.html', {'data':data})

def searchlist(request):
	products = Product.objects.filter().values_list('name', flat=True)
	productslist = list(products)
	print(productslist)
	return JsonResponse(productslist, safe=False)

def singleproduct(request,id):
	single_products = Product.objects.get(id=id)
	return render(request, 'ecom_app/singleproduct.html', {'data':single_products})

def category_products(request, id):
	cat_product = Product.objects.filter(category=id)
	print(cat_product)
	return render(request, 'ecom_app/categoryproduct.html', {'products':cat_product})