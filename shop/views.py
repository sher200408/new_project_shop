from django.shortcuts import render

from shop.models import ShopModels, ProductCategoryModel, ProductImageModel

def products_list_view(request):
    categories = ProductCategoryModel.objects.all()
    shops = ShopModels.objects.all()
    context = {
        "shops": shops,
        "categories": categories,
    }
    return render(request, 'shop/products_list.html', context)

def product_detail_view(request, pk):
    try:
        product = ShopModels.objects.get(id=pk)
    except ShopModels.DoesNotExist:
        return render(request, 'pages/404.html')

    related_product = ShopModels.objects.filter(categories__in =[cat.id for cat in  product.categories.all()]).exclude(id=product.id)

    context = {
        "product": product,
        "related_product":related_product
    }

    return render(request, 'shop/product_detail.html', context)


