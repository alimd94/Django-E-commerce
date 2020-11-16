from django.urls import path
from . import views

app_name = "cart"
urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('add/<int:pk>', views.AddCart.as_view(), name="add"),
    # path('update/<int:pk>', views.UpdateCart.as_view(), name="update"),
    # path('delete/<int:pk>', views.DeleteCart.as_view(), name="delete"),
]
