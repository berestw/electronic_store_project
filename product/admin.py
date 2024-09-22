from django.contrib import admin

from product.models import Products


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    """Интерфейс администрирования продукта для администратора."""
    list_display = ('id', 'name', 'product_models', 'release_date', 'company')
    search_fields = ('name',)
