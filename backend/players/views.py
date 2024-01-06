from .serializers import PlayerSerializer
from rest_framework import viewsets
from .models import Player
from accounts.permissions import IsManagerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class PlayerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsManagerOrReadOnly]
    serializer_class = PlayerSerializer

    def get_queryset(self):
        return Player.objects.all()
