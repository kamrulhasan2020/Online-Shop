from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from .models import Category, Product


class ProductListView(ListView):
    template_name = 'shop/product-list.html'
    context_object_name = 'Products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return self.category.products.filter(available=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Catagory'] = self.category
        return context


class ProductDetailView(DetailView):
    template_name = 'shop/produc-detail.html'
    context_object_name = 'product'

    def get_object(self):
        return get_object_or_404(Product, slug=self.kwargs['slug'])
