from django.urls import path
from store.views import *

urlpatterns=[

path("",ProductListView.as_view(),name="product_list"),
path("<int:pk>",ProductDetailView.as_view(),name="detail"),
path("create",ProductCreateView.as_view(),name="create"),
]

