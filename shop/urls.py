from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('product/', views.product), #<int:pk>
    path('checkout/', views.checkout),
    path('store/', views.store),
]
