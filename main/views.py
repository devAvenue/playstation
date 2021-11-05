from django.shortcuts import render
from .models import *


base_url = 'http://127.0.0.1:8080/'

# Create your views here.
def index(requests):
    basc = cart.objects.filter(session=requests.COOKIES.get('sessionid'))
    return render(requests,'index.html', {'base_url':base_url, 'basket':basc})

def handler404(requests, exception):
    basc = cart.objects.filter(session=requests.COOKIES.get('sessionid'))
    print(exception)
    print(123412432423)
    return render(requests,'index.html', {'base_url':base_url, 'basket':basc})

def contact(requests):
    basc = cart.objects.filter(session=requests.COOKIES.get('sessionid'))
    return render(requests,'contact.html', {'base_url':base_url, 'basket':basc})

def dostavka(requests):
    basc = cart.objects.filter(session=requests.COOKIES.get('sessionid'))
    return render(requests,'dostavka.html', {'base_url':base_url, 'basket':basc})

def oplata(requests):
    basc = cart.objects.filter(session=requests.COOKIES.get('sessionid'))
    return render(requests,'oplata.html', {'base_url':base_url, 'basket':basc})

def garantiya(requests):
    basc = cart.objects.filter(session=requests.COOKIES.get('sessionid'))
    return render(requests,'garantiya.html', {'base_url':base_url, 'basket':basc})

def rekvizity(requests):
    basc = cart.objects.filter(session=requests.COOKIES.get('sessionid'))
    return render(requests,'rekvizity.html', {'base_url':base_url, 'basket':basc})

def get_blog(requests,post):
    basc = cart.objects.filter(session=requests.COOKIES.get('sessionid'))
    post = blog.objects.get(url=post)
    print(post.description)
    return render(requests, 'blog.html', {'base_url': base_url, 'blog': post, 'basket':basc})

def one_blog(requests):
    basc = cart.objects.filter(session=requests.COOKIES.get('sessionid'))
    posts = reversed(blog.objects.all().order_by('date'))
    return render(requests, 'main_blog.html', {'base_url': base_url, 'posts': posts, 'basket':basc})

def main_catalog(requests):
    basc = cart.objects.filter(session=requests.COOKIES.get('sessionid'))
    j_category = categories.objects.all()
    all_products = products.objects.all()
    search = []
    try:
        keyword = requests.GET['keyword']
        if len(keyword) >= 1:
            for i in all_products:
                if keyword in i.name.lower():
                    search.append(i)
            all_products = search
    except:
        pass
    return render(requests, 'main_catalog.html', {'base_url': base_url,'categories':j_category,
                                                  'products':all_products, 'basket':basc})

def catalog(requests, id):
    basc = cart.objects.filter(session=requests.COOKIES.get('sessionid'))
    if str(id) == '':
        main_catalog(requests)
        return
    j_category = categories.objects.all()
    all_products = products.objects.filter(category=categories.objects.get(id=id))
    return render(requests, 'main_catalog.html', {'base_url': base_url,'categories':j_category,'products':all_products, 'basket':basc})

def product(requests, id):
    basc = cart.objects.filter(session=requests.COOKIES.get('sessionid'))
    recommend = products.objects.filter(category=categories.objects.get(id=4))[:5]
    return render(requests, 'product.html',
                  {'base_url': base_url,'product':products.objects.get(id=id),'recommend':recommend, 'basket':basc})

def basket(requests):
    basc = cart.objects.filter(session=requests.COOKIES.get('sessionid'))
    return render(requests, 'basket.html',
                  {'base_url': base_url, 'products':[1], 'basket':basc})

def remove(requests,action,id):
    try:
        if action == 'remove':
            cart.objects.get(id=id).delete()
        elif action =='plus':
            c = cart.objects.get(id=id)
            c.count = c.count+1
            c.save()
        elif action == 'minus':
            c = cart.objects.get(id=id)
            if c.count == 1:
                cart.objects.get(id=id).delete()
            else:
                c.count = c.count-1
                c.save()
    except:pass
    basc = cart.objects.filter(session=requests.COOKIES.get('sessionid'))
    return render(requests, 'basket.html',
                  {'base_url': base_url, 'products':[1], 'basket':basc})

def api(requests):
    basc = cart.objects.filter(session=requests.COOKIES.get('sessionid'))
    if requests.method == 'GET':
        if requests.GET['action'] == 'addbasket':
            cart(session=requests.COOKIES.get('sessionid'), product=products.objects.get(id=str(requests.GET['id'])), count=requests.GET['count']).save()
            return render(requests,'index.html', {'base_url':base_url, 'basket':basc})


from bs4 import BeautifulSoup
import requests

# code = ''''''
# bs = BeautifulSoup(code,'html.parser')
#
# for i in bs.find_all('tr'):
#     price = i.find('div',{'class':'price'}).get_text().replace(' руб.\n', '').replace('\n','').replace(' ','')
#     image_wrapper = list(i.find('div',{'class':'image_wrapper_block'}).find('img').attrs.values())
#     img, name = image_wrapper[0], image_wrapper[1]
#     url = f"https://m-playstation.store/{list(i.find('td', {'class': 'item-name-cell'}).find('a').attrs.values())[1]}"
#     douther = BeautifulSoup(requests.get(url).text, 'html.parser')
#
#     images = douther.find('div', {'class': 'item_slider'})
#     print(images)
#     tabs_section = douther.find('div', {'class':'tabs_section'})
#     description  = douther.find('div', {'class':'preview_text'}).get_text()
#
#     products(category=categories.objects.get(id=9),photo=img,name=name,price=int(price),main_page=url,images=str(images),comments=str(tabs_section), description=description).save()



# from bs4 import BeautifulSoup
# import requests
# for product in products.objects.all():
#     print(product.main_page)
#     bs = BeautifulSoup(requests.get(product.main_page),'html.parser')
#     print(bs.find_all('div',{'class':'item_slider'}))