from django.contrib import admin
from django.urls import path
from product.views import *
from accounts.views import *
from accounts.admin_views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django_email_verification import urls as email_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('signin/', signInPage, name='signin'),
    path('logout/', logoutPage, name='logout'),
    path('signup/', signUpPage, name='signup'),
    path('cart/', cartView, name='cart'),
    path('cart/<id>', addToCart, name='cart'),
    path('<id>', plusCart, name='pluscart'),
    path('minus/<id>', minusCart, name='minuscart'),
    path('remove/<id>', removeCart, name='removecart'),
    path('catgory/<id>', categoryView, name='category'),
    path('checkout/', checkout, name='checkout'),
    path('address_update/<id>', address_form, name='address_update'),
    path('payment/', payment, name='payment'),
    path('charge/', charge, name='charge'),
    path('orders/', orderView, name='orders'),


    #url for eg_Admin
    path('eg_admin/', adminView, name='eg_admin'),
    path('orderview/', orderViewAdmin, name='orderview'),
    path('order_update/<id>', orderForm, name='order_update'),
    path('category_view/', categoryView, name='category_view'),
    path('addcategory/', category_form, name='addcategory'),
    path('category_update/<id>', category_form, name='category_update'),
    path('category_delete/<id>', category_delete, name='category_delete'),
    path('product_view/', productAdminView, name='product_view'),
    path('addproduct/', product_form, name='addproduct'),
    path('product_update/<id>', product_form, name='product_update'),
    path('product_delete/<id>', product_delete, name='product_delete'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="password_reset_done.html"),
         name="password_reset_complete"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
