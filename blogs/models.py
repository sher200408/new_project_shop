from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class BlogHashtagModel(models.Model):
    title = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog hashtag'
        verbose_name_plural = 'blogs hashtags'




class BlogModel(models.Model):
    objects = True
    author = models.ForeignKey(
        User,
            on_delete=models.SET_NULL,
            related_name="blogs",
            null=True,blank=True
    )
    image = models.ImageField(upload_to="blogs")
    title = models.CharField(max_length=255)

    short_description = models.CharField(max_length=255)
    long_description = models.TextField()

    hashtags = models.ManyToManyField(BlogHashtagModel,related_name="blogs")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'


# class ProfilModel(models.Model):
#     avatar = models.ImageField(upload_to='avaters')
#     about = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=128)
#     last_name = models.CharField(max_length=128)
#
#     @property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def __repr__(self):
#         return self.full_name
#
#     def __str__(self):
#         return self.full_name
#
#     class Meta:
#         verboses_name = "profile"f
