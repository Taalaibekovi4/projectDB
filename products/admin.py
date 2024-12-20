from django.contrib import admin
from products.models import Product, ProductImage

# Регистрация модели ProductImage как inline
class ProductImageInline(admin.TabularInline):  # Можно использовать StackedInline, если нужен другой стиль
    model = ProductImage
    extra = 1  # Количество пустых полей для добавления новых изображений

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'category', 'brand']
    inlines = [ProductImageInline]  # Добавляем inline для изображений
