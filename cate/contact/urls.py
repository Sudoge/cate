from django.conf.urls import url
from contact import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
]