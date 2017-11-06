from django.shortcuts import render
from product.models import ProductModel
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    # 查询数据
    prod_list = ProductModel.objects.all()[:6]
    return render(request, 'product/index.html', locals())


def  product_list(request):
    prod_list = ProductModel.objects.all()
    # 分页显示
    num = 6
    index = 1
    paginator = Paginator(prod_list, num)
    page = paginator.page(index)
    print(page.object_list)
    return render(request, 'product/productlist.html', locals())


def about(request):
    return render(request, 'product/about.html', locals())

