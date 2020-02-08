from django.contrib import admin

# Register your models here.
from .models import Position, PositionItem


class PositionAdmin(admin.ModelAdmin):
    list_display = ('lang', 'name', 'order',)
    list_filter = ('order', 'name',)
    search_fields = ('order', 'name',)
    list_editable = ('name', 'order',)


class PositionItemAdmin(admin.ModelAdmin):
    list_display = ('lang', 'titre', 'description', 'audio', 'position','img',)
    list_filter = ('titre', 'description', 'lang', 'audio', 'position','img',)
    search_fields = ('titre', 'description', 'lang', 'audio', 'position','img',)
    list_editable = ('titre', 'description', 'audio', 'position','img',)


admin.site.register(Position, PositionAdmin)

admin.site.register(PositionItem, PositionItemAdmin)
