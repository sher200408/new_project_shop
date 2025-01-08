from django.urls import path

from pages.views import home_page_view, about_page_view, contact_page_view,shop_page_view

app_name = 'pages'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('about/', about_page_view, name='about'),
    path('contact/', contact_page_view, name='contact'),
    path('shop/',shop_page_view,name='shop')
]
