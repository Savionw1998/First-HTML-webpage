from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('register', views.Register),
    path('registration', views.AdminReg),
    path('signin', views.AdminLogin),
    path('login', views.Login),
    path('dashboard/orders', views.DashOrder),
    path('orders/show', views.ShowOrders),
    path('dashboard/products', views.DashProduct),
    path('dashboard/<int:TheProduct>/destroy', views.Kill),
    path('product/edit/<int:TheProduct>', views.EditItemPage),
    path('edit/<int:TheProduct>', views.EditItem),
    path('product/add', views.AddItem),
    path('product/addnew', views.AddItemPage),
    path('items', views.Items),
    path('show/item/<int:product_id>', views.ShowItem),
    path('cart', views.Cart),
]