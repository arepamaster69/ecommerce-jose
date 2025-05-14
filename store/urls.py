from django.urls import path
from store.views import *

urlpatterns=[

path("",ProductListView.as_view(),name="product_list"),
path("<int:pk>",ProductDetailView.as_view(),name="detail"),
path("create",ProductCreateView.as_view(),name="create"),
path("<int:pk>/update",ProductUpdateView.as_view(),name="update"),
path("<int:pk>/delete",ProductDeleteView.as_view(),name="delete")
]
