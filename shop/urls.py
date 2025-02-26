from django.urls import path

from shop.views import products_list_view, product_detail_view

app_name = 'shop'

urlpatterns = [
    path('product/<int:pk>/', product_detail_view, name='products-detail'),
    path('', products_list_view, name='products-list'),
]
