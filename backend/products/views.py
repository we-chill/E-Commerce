from django.http import Http404

from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductListAll(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryDetail(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class ProductDetail(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class ProductCreate(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializers = ProductSerializer(data=request.data, many=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryCreate(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializers = CategorySerializer(data=request.data, many=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
