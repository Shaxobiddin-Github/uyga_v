from django.shortcuts import render,redirect
from django.core.handlers.wsgi import WSGIRequest 
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import permission_required,login_required
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

from .models import Category, News,Comment
from .forms import RegisterForm,LoginForm

@login_required(login_url="login")
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


@login_required
@permission_required('main.view_news')
def detail(request, pk):
    news = News.objects.get(pk=pk)
    categories = Category.objects.all()
    context = {
        "news":news,
        "categories":categories
    }
    return render(request, "blog_details.html",context)




def save_comments(request:WSGIRequest,news_id):
    news= News.objects.get(id=news_id)
    Comment.objects.create(
        user = request.user,
        news = news,  
        text = request.GET.get("text")
    )
    messages.success(request, "Komment qushildi")
    return redirect('detail', pk=news_id)



def register(request:WSGIRequest):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
            " Tabriklaymiz......  \n"
            "  Siz muvaffaqiyatli ruyxatdan utdingiz\n"
            "Login parolni terib saytimizga kiring!")
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
            messages.success(request, f"saytga xush kelibsiz {user.username}")
            return redirect('home')
    login_form = LoginForm()
    context={
        "login_form":login_form,
    }
    return render(request, "login.html",context)

@login_required
def user_logout(request):
    logout(request)
    messages.warning(request, "Siz saytdan muvaffaqiyatli chiqdingiz!!")
    return redirect('login')




@login_required
@permission_required("app.change_news","login")
def change_news(request):
    return  HttpResponse("o'zgartirish")




@login_required
def send_message_to_email(request:WSGIRequest):
    if request.user.is_staff:
        if request.method == "POST":
            title = request.POST.get("title")
            text = request.POST.get("text")
            
            users = User.objects.all()

            send_mail(
                title,
                text,
                settings.EMAIL_HOST_USER,
                [user.email for user in users],
                fail_silently=False,
            )
            messages.success(request, "xabar yuborildi📑")
        return render(request,"send_message.html")
    else:
        page = request.META.get("Http_REFERER", "home")
        return redirect(page)