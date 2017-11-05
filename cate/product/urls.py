from django.conf.urls import url
from product import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^product_list/$', views.product_list, name='product_list'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
]