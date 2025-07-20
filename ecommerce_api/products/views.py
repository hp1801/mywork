from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.core.cache import cache
from django_filters import rest_framework as filters
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .filters import ProductFilter

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category')
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    filter_backends = [filters.DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['price', 'name']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        cache_key = 'products_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = self.get_paginated_response(serializer.data).data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
        cache.set(cache_key, data, timeout=3600)
        return Response(data)

    def perform_create(self, serializer):
        serializer.save()
        cache.delete('products_list')

    def perform_update(self, serializer):
        serializer.save()
        cache.delete('products_list')

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete('products_list')