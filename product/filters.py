import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains', label='')

    class Meta:
        model = Product
        fields = ['title', ]