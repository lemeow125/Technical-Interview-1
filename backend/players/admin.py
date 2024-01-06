from django.contrib import admin
from .models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'age',)


admin.site.register(Player, PlayerAdmin)
