from .models import Player
from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    number = serializers.CharField(required=True)

    class Meta:
        model = Player
        fields = ['id', 'number', 'full_name', 'firstName', 'lastName',
                  'pos', 'bat', 'thw', 'age', 'ht', 'wt', 'birthPlace']
        read_only_fields = ['id', 'timestamp']
