from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product, Brand , Category
# Create your views here.

class ProductList(ListView):
    model = Product
    paginate_by = 50
    extra_context = {'all_count' : Product.objects.all().count()}
    
    
class ProductDetail(DetailView):
    model = Product


class CategoryList(ListView):
    model = Category

class BrandList(ListView):
    model = Brand
    extra_context = {
        'categories' : Category.objects.all() }

class BrandDetail(DetailView):
    model = Product  