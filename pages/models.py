from django.db import models

# Create your models here.
class CantactModel(models.Model):
    objects = True
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    text = models.TextField()


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'