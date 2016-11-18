from django.contrib import admin
from .models import Board


def new_game(modeladmin, request, queryset):
    for board in queryset:
        board.new_game()


new_game.short_description = u'New Game'


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'state']
    list_filter = ['created']
    actions = [new_game]
