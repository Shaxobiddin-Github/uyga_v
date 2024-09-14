from django.shortcuts import render

from .models import Category, News


def index(request):
    newsers = News.objects.filter(is_active = True)
    news_banner = newsers.filter(is_banner=True).last()
    latest_news = newsers.order_by("-created_at").last()
    top_news = newsers.order_by("-views").first()
    latest_newses = newsers.order_by("-created_at")[:8]
    what_news = newsers.filter(tag=3).last()
    what_news_technology = newsers.filter(tag=5).last()
    what_news_diniy = newsers.filter(tag=9).last()
    what_news_sayoxat = newsers.filter(tag=6).last()
    what_news_hayot = newsers.filter(tag=7).last()
    context = {
        "news_banner":news_banner,
        "top_news":top_news,
        "latest_news":latest_news,
        "latest_newses":latest_newses,
        "what_news":what_news,
        "what_news_technology":what_news_technology,
        "what_news_diniy":what_news_diniy,
        "what_news_sayoxat":what_news_sayoxat,
        "what_news_hayot":what_news_hayot,
    }
    return render(request, 'index.html',context)



def about(request):
    return render(request, 'about.html')


def categori(request):
    return render(request, 'categori.html')


def blog_details(request):
    return render(request, 'blog_details.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def elements(request):
    return render(request, 'elements.html')

def latest_news(request):
    return render(request, 'latest_news.html')

def main(request):
    return render(request, 'main.html')



