from django.urls import include, path
from rest_framework_nested import routes

from skymarket.ads.views import AdViewSet, CommentViewSet


ads_router = routes.SimpleRouter()
ads_router.register(r"ads", AdViewSet)

ads_router.register("ads", AdViewSet, basename="users")
comments_router = routes.NestedSimpleRouter(ads_router, r"ads", lookup="ad")
comments_router.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(ads_router.urls)),
    path("", include(comments_router.urls)),
]
