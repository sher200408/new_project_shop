from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('recipies/', include('recipies.urls', namespace='recipies')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('users/', include('users.urls', namespace='users')),
    path('', include('pages.urls', namespace='pages')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
