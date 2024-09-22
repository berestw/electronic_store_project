from django.contrib import admin

from user.models import Users


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    """Интерфейс администрирования"""
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff',
                    'is_superuser')
