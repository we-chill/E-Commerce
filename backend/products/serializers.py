from rest_framework import serializers

from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'get_absolute_url',
            'title',
            'price',
            'description',
            'origin',
            'warranty_expired_date',
            'status',
            'category',
            'get_image',
        ]


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'get_absolute_url',
            'title',
            'products'
        ]
