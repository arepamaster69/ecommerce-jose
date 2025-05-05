from django.urls import path
from store.views import ProductListView

urlpatterns=[

path("",ProductListView.as_view(),name="product_list")

]