from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')



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



