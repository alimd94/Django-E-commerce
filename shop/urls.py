from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('product/', views.product), #<int:pk>
    path('checkout/', views.checkout),
    path('store/', views.store),
]
