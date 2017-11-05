from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', locals())


def  product_list(request):
    return render(request, 'productlist.html', locals())


def about(request):
    return render(request, 'about.html', locals())

def contact(request):
    return render(request, 'contact.html', locals())
