from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shorcuts import get_object_or_404
from .models import Catagory, Product


class ProductListView(ListView):
    template_name = 'shop/product-list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category = get_object_or_404(Catagory, slug=self.kwargs['slug'])
        return category.products.filter(available=True)


class ProductDetailView(DetailView):
    template_name = 'shop/produc-detail.html'
    context_object_name = 'product'

    def get_object(self):
        return get_object_or_404(Product, slug=self.kwargs['slug'])

  
