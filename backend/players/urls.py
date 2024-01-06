from django.urls import path, include
from .views import PlayerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PlayerViewSet, basename="Player Entries")

urlpatterns = [
    path('', include(router.urls)),
]
