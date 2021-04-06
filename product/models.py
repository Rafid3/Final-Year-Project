from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.category
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    product_image = models.ImageField(default="product.jpg", null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    price = models.FloatField('Price : $', null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title



class Cart(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.product.title

    def productTotal(self):
        t = self.product.price * self.quantity
        return t


class Address(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    street = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=14, null=True)

    def __str__(self):
        return self.city


class Order_Product(models.Model):
    CHOICES = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Cancled', 'Cancled'),
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    cartitem = models.ManyToManyField(Cart)
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    status = models.CharField(
        max_length=100, null=True, choices=CHOICES, default=CHOICES[0][0])

    def __str__(self):
        return self.user.first_name

    def orderTotal(self):
        t = 0
        for i in self.cartitem.all():
            t += i.productTotal()
        return t
