from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from company.models import Company, Supplier
from company.paginators import CompanyPaginator, SuppliersPaginator
from company.permissions import IsCompanyOwner, IsSupplierOwner

from company.serializers import CompanySerializer, CompanyDetailSerializer, CompanyListSerializer, \
    CompanyUpdateSerializer, SupplierSerializer, SupplierListSerializer, SupplierUpdateSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """Набор представлений компании"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = CompanyPaginator
    filter_backends = (filters.SearchFilter,)
    search_fields = ("country",)

    def get_permissions(self):
        """Проверка доступа компании"""
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
            self.serializer_class = CompanySerializer
        if self.action in ["list"]:
            self.permission_classes = [AllowAny]
            self.serializer_class = CompanyListSerializer
        if self.action in ["retrieve"]:
            self.permission_classes = [IsAuthenticated, IsCompanyOwner]
            self.serializer_class = CompanyDetailSerializer
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [IsAuthenticated, IsCompanyOwner]
            self.serializer_class = CompanyUpdateSerializer
        return super().get_permissions()

    def perform_create(self, serializer):
        """Создание компании из сериализатора"""
        company = serializer.save()
        company.owner = self.request.user
        company.save()
        return company


class SupplierViewSet(viewsets.ModelViewSet):
    """Набор представлений поставщика"""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    pagination_class = SuppliersPaginator

    def get_permissions(self):
        """Проверка доступа поставщика"""
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        if self.action == "list":
            self.permission_classes = [IsAuthenticated]
            self.serializer_class = SupplierListSerializer
        if self.action in ["retrieve"]:
            self.permission_classes = [IsAuthenticated, IsSupplierOwner]
            self.serializer_class = SupplierSerializer
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [IsAuthenticated, IsSupplierOwner]
            self.serializer_class = SupplierUpdateSerializer
        return super().get_permissions()

    def perform_create(self, serializer):
        """Перед сохранением поставщика, добавляем владельца"""
        supplier = serializer.save()
        customer = Company.objects.get(id=supplier.customer)
        supplier.owner = self.request.user
        supplier.save()

        if customer.type_company == 'individual_entrepreneur' or customer.type_company == 'retail_chain':
            Company.objects.filter(id=customer.id).update(
                level_company=2, name=supplier.supplier.name,
                supplier_id=supplier.supplier.id,
            )
            supplier.name = customer.name
            supplier.owner = self.request.user
            supplier.save()
        elif customer.type_company == 'factory':
            supplier.name = customer.name
            supplier.save()
            Company.objects.filter(id=customer.id).update(
                level_company=1, name=supplier.supplier.name,
                supplier_id=supplier.supplier.id
            )
        return supplier

    def perform_update(self, serializer):
        """Перед сохранением поставщика, добавляем владельца"""
        supplier = serializer.save()
        customer = Company.objects.get(id=supplier.customer)

        if customer.type_company == 'individual_entrepreneur' or customer.type_company == 'retail_chain':
            supplier.name_supplier = customer.name
            supplier.owner = self.request.user
            supplier.save()
            Company.objects.filter(id=customer.id).update(
                level_company=2, name=supplier.supplier.name,
                supplier_id=supplier.supplier.id,
            )
        elif customer.type_company == 'factory':
            supplier.name = customer.name
            supplier.owner = self.request.user
            supplier.save()
            Company.objects.filter(id=customer.id).update(
                level_company=1, name=supplier.supplier.name,
                supplier_id=supplier.supplier.id
            )
        return supplier
