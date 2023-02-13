from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product 
# Create your views here.

class ProductList(ListView):
    model = Product
    paginate_by = 50
    extra_context = {'all_count' : Product.objects.all().count()}
    
    
class ProductDetail(DetailView):
    model = Product