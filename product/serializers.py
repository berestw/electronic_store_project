from rest_framework import serializers

from product.models import Products


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор объектов продукта."""

    class Meta:
        model = Products
        fields = "__all__"
        read_only_fields = ["arrears"]


class ProductListSerializer(serializers.ModelSerializer):
    """Сериализатор списка продуктов."""

    class Meta:
        model = Products
        fields = ("id", "name", "product_models", "release_date", "company")


class ProductDetailSerializer(serializers.ModelSerializer):
    """Сериализатор объектов продуктов."""

    class Meta:
        model = Products
        fields = "__all__"


class ProductUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор обновления продукта"""

    class Meta:
        model = Products
        fields = "__all__"
