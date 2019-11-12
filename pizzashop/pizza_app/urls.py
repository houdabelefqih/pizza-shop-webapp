from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('register/', views.register, name='register'),
    path('cart/', views.display_cart, name='display-cart'),
    path('orders/', views.display_orders, name='display-orders'),
    path('order/', views.start_order, name='start-order'),
    path('', views.index, name='index'),



]
