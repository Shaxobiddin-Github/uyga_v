
from django.shortcuts import render,redirect
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import login, logout

from .models import Category, News
from .forms import RegisterForm,LoginForm


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
    newsers = News.objects.filter(is_active = True)
    latest_news = newsers.order_by("-created_at").last()

    context = {
        "latest_news":latest_news,
    }
    return render(request, 'latest_news.html')

def main(request):
    return render(request, 'main.html')



def detail(request, pk):
    news = News.objects.get(pk=pk)
    categories = Category.objects.all()
    context = {
        "news":news,
        "categories":categories
    }
    return render(request, "blog_details.html",context)


def register(request:WSGIRequest):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.error_messages, "**********************************")

    else:
        form = RegisterForm()

    context={
        "form":form,
    }
    return render(request, "register.html", context)


def user_login(request:WSGIRequest):
    if request.method == "POST":
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user=login_form.get_user()
            login(request,user)
            return redirect('home')
    login_form = LoginForm()
    context={
        "login_form":login_form,
    }
    return render(request, "login.html",context)


def user_logout(request):
    logout(request)
    return redirect('login')