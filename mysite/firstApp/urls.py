from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('menu/admin',views.menu_admin, name='menu'),
    path('menu/admin/edit/<int:id>',views.Edit_menu),
    path('signin',views.signin, name='signin'),
    path('signup',views.signup),
    path('menu/admin/edit/status',views.menu_item_status, name='item-status'),
    path('logout',views.logout, name="logout"),
    path('customer/menu',views.menu_customer,name='customer-menu'),
    path('customer/cart',views.cart_list_customer),
    path('customer/cart/delete/<int:id>',views.delete_cart_item, name="customer-cart-delete"),
    path('customer/cart/add/<int:id>/<str:name>/<str:price>/<str:category>/<str:delivery>',views.cart_list_customer_add, name="customer-cart-add"),
] 

