from django.db import models


class ProductCategoryModel(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ShopModels(models.Model):
    title = models.CharField(max_length=128, null=True, blank=True)
    price = models.CharField(max_length=100, default='min-mun=10.00')
    images = models.ImageField(upload_to="shop_products")
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    is_stock = models.BooleanField(default=True)
    sku = models.CharField(max_length=10, unique=True)
    categories = models.ManyToManyField(ProductCategoryModel, related_name="products")

    class Meta:
        db_table = 'shop_blog'


class ProductImageModel(models.Model):
    product_shop = models.ForeignKey(ShopModels, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='products')
