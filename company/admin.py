from django.contrib import admin

from company.models import Supplier, Company


def clear_debt(queryset):
    for obj in queryset:
        obj.debt = 0
        obj.save()


clear_debt.short_description = "Очистить задолженность"

fields_display = [
    'name',
    'debt',
    'customer',
    'supplier',
    'owner',
]


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Интерфейс администратора для поставщика."""
    list_display = fields_display
    actions = [clear_debt]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Интерфейс администрирования компании для администратора."""
    list_display = ('id', 'name', 'email', 'country', 'town', 'type_company', 'house_number', 'street',
                    'owner')
    search_fields = ('town',)
