from rest_framework.routers import DefaultRouter
from .views import GameViewSet, CategoryViewSet, PlatformViewSet, OrderViewSet

router = DefaultRouter()
router.register('games', GameViewSet)
router.register('categories', CategoryViewSet)
router.register('platforms', PlatformViewSet)
router.register('orders', OrderViewSet)

urlpatterns = router.urls