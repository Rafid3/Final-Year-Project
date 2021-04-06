from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from product.models import *
from .forms import *
from .filters import *
from .forms import *
from .filters import *
from .decorators import *
# Create your views here.
@allowed_users(allowed_roles=['admin'])
def orderViewAdmin(request):
    orders = Order_Product.objects.all().filter(ordered=True).order_by('-id')
    mFilter = OrderFilter(request.GET, queryset=orders)
    orders = mFilter.qs
    context = {
        'orders': orders,
        'mFilter': mFilter
    }

    return render(request, 'admin/orderview.html', context)

@allowed_users(allowed_roles=['admin'])
def orderForm(request, id=id):

    if request.method == "GET":
        if id == 0:
            form = OrderStatusForm()
        else:
            order = Order_Product.objects.get(id=id)
            form = OrderStatusForm(instance=order)
        return render(request, "admin/order_form.html", {'form': form})
    else:
        if id == 0:
            form = OrderStatusForm(request.POST)
        else:
            order = Order_Product.objects.get(id=id)
            form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('orderview')



# Create your views here.
@login_required
@allowed_users(allowed_roles=['admin'])
def adminView(request):

    orders = Order_Product.objects.all().filter(ordered=True).order_by('-id')
    total_orders = orders.count()
    out_orders = Order_Product.objects.all().filter(
        ordered=True, status='Delivered')
    for_delivery = out_orders.count()
    pending_orders = Order_Product.objects.all().filter(
        ordered=True, status='Pending')
    pending = pending_orders.count()

    product = Product.objects.all().order_by('-id')
    context = {
        'product': product,
        'total_orders': total_orders,
        "pending": pending,
        'for_delivery': for_delivery,
        "pending_orders": pending_orders,
    }
    return render(request, 'admin/dashboard.html', context)


@allowed_users(allowed_roles=['admin'])
def productAdminView(request):
    product = Product.objects.all().order_by('-id')
    mFilter = ProductFilter(request.GET, queryset=product)
    product = mFilter.qs
    context = {
        'product': product,
        'mFilter': mFilter
    }
    return render(request, 'admin/product_admin.html', context)


@allowed_users(allowed_roles=['admin'])
def product_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            product = Product.objects.get(id=id)
            form = ProductForm(instance=product)
        return render(request, "admin/product_form.html", {'form': form})
    else:
        if id == 0:
            form = ProductForm(request.POST,request.FILES)
        else:
            product = Product.objects.get(id=id)
            form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
        return redirect('product_view')


@allowed_users(allowed_roles=['admin'])
def product_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product_view')


@allowed_users(allowed_roles=['admin'])
def categoryView(request):
    category = Category.objects.all()
    mFilter = CategoryFilter(request.GET, queryset=category)
    category = mFilter.qs
    context = {
        'category': category,
        'mFilter': mFilter
    }
    return render(request, 'admin/category_admin.html', context)


@allowed_users(allowed_roles=['admin'])
def category_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CategoryForm()
        else:
            category = Category.objects.get(id=id)
            form = CategoryForm(instance=category)
        return render(request, "admin/category_form.html", {'form': form})
    else:
        if id == 0:
            form = CategoryForm(request.POST)
        else:
            category = Category.objects.get(id=id)
            form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        return redirect('category_view')


@allowed_users(allowed_roles=['admin'])
def category_delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('category_view')






