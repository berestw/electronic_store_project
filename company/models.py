from django.db import models

from user.models import Users

SUPPLIERS_TYPE = [('factory', 'завод'), ('retail_chain', 'розничная сеть'), ('individual_entrepreneur', 'индивидуальный предприниматель'), ]
NULLABLE = {'blank': True, 'null': True}


class Company(models.Model):
    """Модель компании."""
    name = models.CharField(unique=True, max_length=255, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    country = models.CharField(max_length=25, verbose_name='Страна')
    town = models.CharField(max_length=25, verbose_name='Город')
    street = models.CharField(max_length=25, verbose_name='Улица')
    house_number = models.CharField(max_length=25, verbose_name='Номер дома')
    level_company = models.IntegerField(default=25, verbose_name='Уровень компании')
    type_company = models.CharField(max_length=25, choices=SUPPLIERS_TYPE, verbose_name='Тип компании')
    supplier_name = models.CharField(max_length=25, verbose_name='Имя поставщика', **NULLABLE)
    supplier_id = models.IntegerField(verbose_name='id поставщика', **NULLABLE)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Supplier(models.Model):
    """Модель поставщика"""
    name = models.CharField(max_length=100, verbose_name='Имя поставщика', **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='задолженность')
    release = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    customer = models.IntegerField(verbose_name='Заказчик')
    supplier = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Поставщик')
    owner = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'
