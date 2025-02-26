from django.contrib import admin

from shop.models import ShopModels, ProductCategoryModel, ProductImageModel


# Register your models here.
# admin.site.register(ShopModels)

@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']


class ProductImageModelAdmin(admin.StackedInline):
    model = ProductImageModel


@admin.register(ShopModels)
class ShopModelsAdmin(admin.ModelAdmin):
    list_display = ['title','price']
    list_filter = ['price']
    search_fields = ['title']
    inlines = [ProductImageModelAdmin]

