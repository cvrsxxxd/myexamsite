from django.urls import path
from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.index, name='index'),
    path('register.html/', views.registerPage, name='register'),
    path('index.html/', views.index, name='index'),
    path('cart.html/', views.cart, name='cart'),
    path('blog.html/', views.blog, name='blog'),
    path('contact.html/', views.contact, name='contact'),
    path('product.html/', views.product, name='product'),
    path('regular.html/', views.regular, name='regular'),
    path('shop.html/', views.shop, name='shop'),
    path('blog_single.html/', views.singleblog, name='blog-single'),
]