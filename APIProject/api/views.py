from django.shortcuts import render, HttpResponse, redirect
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.

def article_list(request):

    # get all articles
    if request.method == "GET":
        articles = Article.objects.all()

    # return render('It is working')

