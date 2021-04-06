import django_filters
from product.models import *

class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Order_Product
        fields = ['status', ]


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains', label='Search By Name')

    class Meta:
        model = Product
        fields = ['category', ]


class CategoryFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(
        field_name='category', lookup_expr='icontains', label='Search Category')

    class Meta:
        model = Category
        fields = ['category', ]

