from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    # product = serializers.StringRelatedField(many=False)

    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product',
            'quantity',
        ]


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=False)

    class Meta:
        model = Order
        fields = [
            'id',
            'address',
            'date',
            'mobile',
            'discount',
            'total_price',
            'status',
            'order_items',
        ]

    def create(self, validated_data):
        order_items = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for item in order_items:
            OrderItem.objects.create(order=order, **item)
        return order
