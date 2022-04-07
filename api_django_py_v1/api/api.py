from rest_framework import viewsets
from api.serializers import CategorySerializer
from api.models import Category
from api.serializers import ProductSerializer
from api.models import Product


class CategoryViewSet(viewsets.ModelViewSet):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()