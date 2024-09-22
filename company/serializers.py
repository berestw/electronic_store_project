from rest_framework import serializers

from company.models import Company, Supplier


class CompanySerializer(serializers.ModelSerializer):
    """Сериализатор объектов компании."""

    class Meta:
        model = Company
        fields = "__all__"


class CompanyListSerializer(serializers.ModelSerializer):
    """Сериализатор списка компаний."""

    class Meta:
        model = Company
        fields = ("id", "name", "email", "country", "town", "street", "house_number", "owner")


class CompanyDetailSerializer(serializers.ModelSerializer):
    """Сериализатор сведений компании."""

    class Meta:
        model = Company
        fields = "__all__"


class CompanyUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор обновления компании."""

    class Meta:
        model = Company
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    """Сериализатор объектов поставщика."""

    class Meta:
        model = Supplier
        fields = "__all__"


class SupplierUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор обновления поставщика."""
    class Meta:
        model = Supplier
        fields = ('customer', 'supplier', 'debt')


class SupplierListSerializer(serializers.ModelSerializer):
    """Сериализатор списка поставщиков."""
    class Meta:
        model = Supplier
        fields = ('name', 'owner', 'id')
