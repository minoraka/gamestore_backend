from rest_framework.routers import DefaultRouter
from .views import GameViewSet, CategoryViewSet, PlatformViewSet, OrderViewSet
from .views import GameViewSet, PublisherViewSet, TagViewSet, DiscountViewSet, DLCViewSet

router = DefaultRouter()
router.register('games', GameViewSet)
router.register('categories', CategoryViewSet)
router.register('platforms', PlatformViewSet)
router.register('orders', OrderViewSet)

urlpatterns = router.urls


router = DefaultRouter()
router.register('games', GameViewSet)
router.register('publishers', PublisherViewSet)
router.register('tags', TagViewSet)
router.register('discounts', DiscountViewSet)
router.register('dlcs', DLCViewSet)

urlpatterns = router.urls