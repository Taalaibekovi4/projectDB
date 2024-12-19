from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


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


def product_get(request):

    if request.method == 'GET':
        products = Product.objects.all()
        data = list(products.values())
        return JsonResponse(data, safe=False)




class ProductAdminView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
