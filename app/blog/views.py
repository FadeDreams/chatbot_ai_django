from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'blog/index.html')


def specific(request):
    return HttpResponse("Hello, world. You're at the blog specific.")


def article(request, article_id):
    return render(request, 'blog/article.html', {'article_id': article_id})
    # return HttpResponse(f"{article_id}")

def getRes(request):
    pass