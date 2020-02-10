from django.contrib import admin

# Register your models here.
from .models import Position, PositionItem


class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'isActive', )
    list_filter = ('order', 'name', 'isActive', )
    search_fields = ('order', 'name', 'isActive', )
    list_editable = ('order', 'isActive', )


class PositionItemAdmin(admin.ModelAdmin):
    list_display = ('lang','position', 'titre', 'description', 'audio', )
    list_filter = ('titre', 'description', 'lang', 'audio', 'position',)
    search_fields = ('titre', 'description', 'lang', 'audio', 'position', )
    list_editable = ('titre', 'description', 'audio', 'position', )


admin.site.register(Position, PositionAdmin)

admin.site.register(PositionItem, PositionItemAdmin)
