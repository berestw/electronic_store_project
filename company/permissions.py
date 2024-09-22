from rest_framework import permissions


class IsCompanyOwner(permissions.BasePermission):
    """Проверяет, является ли пользователь представителем компании"""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsSupplierOwner(permissions.BasePermission):
    """Проверяет, является ли пользователь поставщиком"""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
