from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from store.views import (
    GameViewSet, CategoryViewSet, PlatformViewSet, OrderViewSet,
    PublisherViewSet, TagViewSet, DiscountViewSet, DLCViewSet
)


router = routers.DefaultRouter()
router.register("games", GameViewSet)
router.register("categories", CategoryViewSet)
router.register("platforms", PlatformViewSet)
router.register("publishers", PublisherViewSet)
router.register("tags", TagViewSet)
router.register("discounts", DiscountViewSet)
router.register("dlcs", DLCViewSet)
router.register("orders", OrderViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  
]

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="GameStore API",
        default_version="v1",
        description="API для GameStore проекта",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
]


from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("", RedirectView.as_view(url="/api/", permanent=False)),  
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]



