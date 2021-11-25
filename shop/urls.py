from django.urls import path
from .import views

app_name = 'shop'

urlpatterns = [
    path('<slug:slug>/product-list/', views.ProductListView.as_view(),
         name='product_list'),
    path('<slug:slug>/detail/', views.ProductDetailView.as_view(),
         name='product_detail'),
]
