from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Game, Category, Platform, Order, OrderItem, Publisher, Tag, Discount, DLC
from .serializers import (
    GameSerializer, CategorySerializer, PlatformSerializer,
    OrderSerializer, PublisherSerializer, TagSerializer,
    DiscountSerializer, DLCSerializer
)


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filterset_fields = ["category", "platform", "publisher", "tags"]
    search_fields = ["title", "description"]
    ordering_fields = ["price", "created_at"]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class DLCViewSet(viewsets.ModelViewSet):
    queryset = DLC.objects.all()
    serializer_class = DLCSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=["post"])
    def add_to_cart(self, request):
        game_id = request.data.get("game_id")
        quantity = int(request.data.get("quantity", 1))

        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return Response({"error": "Game not found"}, status=404)

        
        order, _ = Order.objects.get_or_create(is_paid=False)

        
        item, created = OrderItem.objects.get_or_create(order=order, game=game)
        if not created:
            item.quantity += quantity
            item.save()

        return Response({"message": "Added to cart"})

    @action(detail=False, methods=["get"])
    def cart(self, request):
        order = Order.objects.filter(is_paid=False).first()
        if not order:
            return Response({"cart": []})
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    @action(detail=False, methods=["post"])
    def remove_from_cart(self, request):
        game_id = request.data.get("game_id")
        order = Order.objects.filter(is_paid=False).first()
        if order:
            OrderItem.objects.filter(order=order, game_id=game_id).delete()
        return Response({"message": "Removed from cart"})