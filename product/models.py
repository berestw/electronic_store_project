from django.db import models

from company.models import Company


class Products(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=255, verbose_name='Название')
    product_models = models.CharField(max_length=100, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата релиза')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='компания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
