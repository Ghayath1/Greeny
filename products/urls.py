from django.urls import path
from .views import ProductList,ProductDetail


app_name = 'products'


urlpatterns = [
    path('' , ProductList.as_view()),
    path('<slug:slug>', ProductDetail.as_view()),
   
]