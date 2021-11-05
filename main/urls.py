from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact', views.contact),
    path('dostavka', views.dostavka),
    path('oplata', views.oplata),
    path('rekvizity', views.rekvizity),
    path('garantiya', views.garantiya),

    path('blog', views.one_blog),
    path('blog/<str:post>', views.get_blog),

    path('catalog/', views.main_catalog),
    path('catalog/<str:id>', views.catalog),

    path('products/<str:id>', views.product),
    path('cart', views.basket),
    path('cart/<str:action>/<str:id>', views.remove),
    path('api', views.api),
    path('404/',views.handler404)
    # path('profile/<str:username>', views.profile, name="profile"),
    # path('post/<int:id>', views.publicate, name="post"),
]
