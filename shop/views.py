from django.shortcuts import render

from shop.models import ShopModels


def products_list_view(request):
    shops = ShopModels.objects.all()
    context = {
        "shops": shops
    }
    return render(request, 'shop/products_list.html',context)

