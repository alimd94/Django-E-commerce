from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('product/<int:pk>/', views.ProductDetail.as_view()), #<int:pk>
    path('checkout/', views.checkout),
    path('store/', views.store, name="store"),
]
