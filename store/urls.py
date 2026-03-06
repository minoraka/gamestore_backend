
from rest_framework import routers
from .views import GameViewSet, CategoryViewSet, PlatformViewSet, OrderViewSet, PublisherViewSet, TagViewSet, DiscountViewSet, DLCViewSet

router = routers.DefaultRouter()
router.register("games", GameViewSet)
router.register("categories", CategoryViewSet)
router.register("platforms", PlatformViewSet)
router.register("publishers", PublisherViewSet)
router.register("tags", TagViewSet)
router.register("discounts", DiscountViewSet)
router.register("dlcs", DLCViewSet)
router.register("orders", OrderViewSet)

urlpatterns = router.urls