
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ='index' ),
    path('account/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
