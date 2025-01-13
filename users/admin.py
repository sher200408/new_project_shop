from django.contrib import admin

from users.models import CustomUserModel


# Register your models here.
@admin.register(CustomUserModel)
class Admin(admin.ModelAdmin):
    list_display = ['username','email','is_active','date_joined']
    search_fields = ['username']
    list_filter = ['date_joined']



# link = "https://n55.uz/confirm/email/user_id/token/"

