from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics
from django.shortcuts import render

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Поиск
class ProductSearchView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        query = self.request.query_params.get('q', None)
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

def product_list(request):
    products = Product.objects.all()  # Получаем все продукты из базы данных
    return render(request, 'products/product_list.html', {'products': products})