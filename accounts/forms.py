
from django import forms
from product.models import *

class OrderStatusForm(forms.ModelForm):

    class Meta:
        model = Order_Product
        fields = ('status',)

    def __init__(self, *args, **kwargs):
        super(OrderStatusForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "update status"

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'title': 'Product Name',
            'price': 'Price(BDT)',
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select Category"


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('category',)
        labels = {
            'category': 'Category Name',
        }