from django.shortcuts import render
from store.models import Product
from django.views.generic import ListView,DetailView
# Create your views here.

class ProductListView(ListView):
    model=Product
    template_name="list_products.html"
    context_object_name="products"

class ProductDetailView(DetailView):
    model=Product
    template_name="product_detail.html"
    context_object_name="product"