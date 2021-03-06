from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('register/', views.register, name='register'),
    path('cart/', views.display_cart, name='display-cart'),
    path('delete/<int:cart_item_id>/', views.delete_cart_item, name='delete-cart-item'),
    path('orders/', views.display_orders, name='display-orders'),
    path('order/', views.add_to_cart, name='add-order'),
    path('', views.index, name='index'),



]
