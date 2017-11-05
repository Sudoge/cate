from django.conf.urls import url
from article import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^article_list/$', views.article_list, name='article_list'),
]