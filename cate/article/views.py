from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'article.html', locals())


def article_list(request):
    return render(request, 'article_list_content.html', locals())
