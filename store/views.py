from django.shortcuts import render
from store.models import Product
from django.views.generic import ListView,DetailView,CreateView
from django.urls import reverse_lazy
# Create your views here.

class ProductListView(ListView):
    model=Product
    template_name="list_products.html"
    context_object_name="products"

class ProductDetailView(DetailView):
    model=Product
    template_name="product_detail.html"
    context_object_name="product"

class ProductCreateView(CreateView):
    model=Product
    template_name="product_create.html"
    fields="__all__"
    success_url=reverse_lazy("product_list")
