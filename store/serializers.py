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


from rest_framework import serializers
from .models import Game, Category, Platform, Publisher, Tag


class GameSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True
    )

    publisher_id = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(),
        source="publisher",
        write_only=True
    )

    platform_ids = serializers.PrimaryKeyRelatedField(
        queryset=Platform.objects.all(),
        many=True,
        source="platform",
        write_only=True
    )

    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        source="tags",
        write_only=True
    )

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