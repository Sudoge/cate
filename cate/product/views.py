from django.shortcuts import render
from product.models import ProductModel, BannerModel
from django.core.paginator import Paginator
from common.pack_original import get_param
# Create your views here.

def index(request):
    # 取出最新更新的美食
    new_list = ProductModel.objects.get_new_food()
    # 取出点击量较多的美食
    higher_rate_list = ProductModel.objects.higher_rate()
    # 取出最新的广告横幅
    new_banner_list = BannerModel.objects.get_new_banner()
    return render(request, 'product/index.html', locals())


def  product_list(request):
    prod_list = ProductModel.objects.all()
    # 分页显示所有商品
    page_num = get_param(request, 'page')
    num = 6  # 每一页显示美食个数
    paginator = Paginator(prod_list, num)
    page = paginator.page(page_num)
    # 推荐商品
    new_list = ProductModel.objects.get_new_food()
    higher_rate_list = ProductModel.objects.higher_rate()
    new_banner_list = BannerModel.objects.get_new_banner()

    return render(request, 'product/productlist.html', locals())


def about(request):
    return render(request, 'product/about.html', locals())

