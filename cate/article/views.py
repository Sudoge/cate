from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'article/article.html', locals())


def article_list(request):
    return render(request, 'article/article_list_content.html', locals())
