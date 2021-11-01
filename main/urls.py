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
    path('catalog/<str:category>', views.catalog)

    # path('products/<str:username>', views.products),
    #
    # path('profile/<str:username>', views.profile, name="profile"),
    # path('post/<int:id>', views.publicate, name="post"),
]
