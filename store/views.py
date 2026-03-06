from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
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
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer