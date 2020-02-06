from django.contrib import admin

# Register your models here.
from .models import Position, PositionItem


class PositionAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'img',)
    list_filter = ('order', 'name', 'img',)
    search_fields = ('order', 'name', 'img',)


class PositionItemAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'lang', 'audio', 'position',)
    list_filter = ('titre', 'description', 'lang', 'audio', 'position',)
    search_fields = ('titre', 'description', 'lang', 'audio', 'position',)


admin.site.register(Position, PositionAdmin)
admin.site.register(PositionItem, PositionItemAdmin)
