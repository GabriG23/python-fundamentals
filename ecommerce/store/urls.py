from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('product_list/', views.product_list, name='product_list'),
    path('price_chart/', views.product_price_chart, name='price_chart'),
]