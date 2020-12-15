from django.urls import path
from . import views

app_name = "compare"
urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('add/<int:pk>', views.AddCompare.as_view(), name="add"),
    path('delete/<int:pk>', views.DeleteCompare.as_view(), name="delete"),
]
