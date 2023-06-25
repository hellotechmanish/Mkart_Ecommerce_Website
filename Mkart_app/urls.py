# from django import views

from Mkart_app import views
from django.urls import include, path

urlpatterns = [
  path('', views.home, name='home'),
  path('account', views.account, name='account'),
  path('cart', views.cart, name='cart'),
  path('contact', views.contact, name='contact'),
  path('about', views.about, name='about'),
]
