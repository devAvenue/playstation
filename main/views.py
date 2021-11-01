from django.shortcuts import render
from .models import *

base_url = 'http://127.0.0.1:7010/'

# Create your views here.
def index(requests):
    return render(requests,'index.html', {'base_url':base_url})

def contact(requests):
    return render(requests,'contact.html', {'base_url':base_url})

def dostavka(requests):
    return render(requests,'dostavka.html', {'base_url':base_url})

def oplata(requests):
    return render(requests,'oplata.html', {'base_url':base_url})

def garantiya(requests):
    return render(requests,'garantiya.html', {'base_url':base_url})

def rekvizity(requests):
    return render(requests,'rekvizity.html', {'base_url':base_url})

def get_blog(requests,post):
    post = blog.objects.get(url=post)
    print(post.description)
    return render(requests, 'blog.html', {'base_url': base_url, 'blog': post})

def one_blog(requests):
    posts = reversed(blog.objects.all().order_by('date'))
    return render(requests, 'main_blog.html', {'base_url': base_url, 'posts': posts})

def main_catalog(requests):
    category = categories.objects.all()
    return render(requests, 'main_catalog.html', {'base_url': base_url,'categories':category})

def catalog(requests, category):
    print(requests)
    if str(category) == '':
        main_catalog(requests)
        return
    category = categories.objects.all()
    return render(requests, 'main_catalog.html', {'base_url': base_url,'categories':category})