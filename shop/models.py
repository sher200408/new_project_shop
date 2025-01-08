from django.db import models



# Create your models here.
class ShopModels(models.Model):
    objects = True
    title = models.CharField(max_length=128, null=True, blank=True)
    price = models.CharField(max_length=100, default='min-mun=10.00')
    image = models.ImageField(upload_to="shop")

    class Meta:
        db_table = 'shop_blog'
