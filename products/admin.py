from django.contrib import admin
from .models import Product



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'category', 'brand', 'get_media_url']


    def get_media_url(self, obj):
        return obj.media_url  # Возвращаем значение поля media_url

    get_media_url.short_description = 'Media URL'  # Переименование столбца в админке
