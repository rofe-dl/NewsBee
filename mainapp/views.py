from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from . import mediastack

from user_auth.models import SharedNews

from datetime import datetime
import time

def get_user_articles(request):
    articles_shared = []
    for article in SharedNews.objects.filter(user=request.user.id).order_by('-datetime_shared'): # - to sort desc
        articles_shared.append({

            'caption' : article.caption,
            'source' : article.source,
            'published_at' : article.published_at,
            'url' : article.url,
            'title' : article.title,
            'description' : article.description,
            'image' : article.image,
            'author' : article.author,
            'category' : article.category,
            'datetime_shared' : article.datetime_shared,
            'full_name' : article.full_name
        })
    
    return articles_shared

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user_auth:login"))

    # communicates with the api and gets the news by country for home page
    country_code = request.user.user_profile.country
    mediastack.country_code = country_code
    articles = mediastack.get_by_country()

    return render(request, "mainapp/news.html", {
        "articles" : articles,
    })

def share_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user_auth:login"))

    article = article = {
        'source' : request.POST["source"],
        'published_at' : request.POST["published_at"],
        'url' : request.POST["url"],
        'title' : request.POST["title"],
        'description' : request.POST["description"],
        'image' : request.POST["image"],
        'author' : request.POST["author"],
        'category' : request.POST["category"],
        'full_name' : request.user.first_name
    }

    return render(request, 'mainapp/share.html',{
        'article' : article
    })


def my_collection_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user_auth:login"))
    
    if request.method == "POST": #POST means user just shared something and redirected here
        
        shared_news = SharedNews()
        
        shared_news.image = request.POST["image"]
        shared_news.url = request.POST["url"]
        shared_news.author = request.POST["author"]
        shared_news.title = request.POST["title"]
        shared_news.description = request.POST["description"]
        shared_news.source = request.POST["source"]
        shared_news.category = request.POST["category"]
        shared_news.published_at = request.POST["published_at"]
        shared_news.datetime_shared = str(datetime.fromtimestamp(time.time()))[0:-7] #to cut milliseconds from time
        shared_news.caption = request.POST["caption"]
        shared_news.full_name = request.user.first_name
        
        shared_news.save() #must save before adding to a ManyToMany field according to django docs

        shared_news.user.add(User.objects.get(username=request.user.username) )
        
        shared_news.save()
        request.user.save()

        return HttpResponseRedirect(reverse('mainapp:my_collection'))

    else:

        articles_shared = get_user_articles(request)

        return render(request, 'mainapp/my_collection.html',{
            'articles' : articles_shared,
        })

def delete_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user_auth:login"))

    datetime_shared = request.POST["datetime_shared"]
    url = request.POST["url"]

    query = SharedNews.objects.filter(datetime_shared=datetime_shared, url=url, user=request.user.id)
    query.delete()

    return HttpResponseRedirect(reverse("mainapp:my_collection"))


def bee_news_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user_auth:login"))

    articles_shared = []

    for article in SharedNews.objects.exclude(user=request.user.id).order_by('-datetime_shared'): # - to sort desc
        articles_shared.append({

            'caption' : article.caption,
            'source' : article.source,
            'published_at' : article.published_at,
            'url' : article.url,
            'title' : article.title,
            'description' : article.description,
            'image' : article.image,
            'author' : article.author,
            'category' : article.category,
            'datetime_shared' : article.datetime_shared,
            'full_name' : article.full_name
        })

    return render(request, 'mainapp/bee_news.html',{
        'articles' : articles_shared,
    })

def search_news_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user_auth:login"))

    keyword = request.POST["keyword"]
    articles = mediastack.get_by_keyword(keyword.strip())

    return render(request, "mainapp/news.html", {
        "articles" : articles,
        "keyword_entered" : keyword
    })

def search_my_collection_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user_auth:login"))

    keyword = request.POST["keyword"]
    keyword_upper = keyword.upper()
    articles_shared = get_user_articles(request)
    articles_filtered = []

    for article in articles_shared:
        
        if keyword_upper in article['title'].upper() or keyword_upper in article['description'].upper():
            articles_filtered.append(article)
    
    return render(request, "mainapp/my_collection.html", {
        "articles" : articles_filtered
    })