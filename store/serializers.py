from rest_framework import serializers
from .models import Game, Category, Platform, Order, OrderItem, Publisher, Tag, Discount, DLC


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ["id", "name"]


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["id", "name", "website"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"


class DLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = DLC
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    publisher = PublisherSerializer(read_only=True)
    platform = PlatformSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "game", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "user", "is_paid", "created_at", "items"]
        read_only_fields = ["user"]