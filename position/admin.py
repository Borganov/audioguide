from django.contrib import admin

# Register your models here.
from .models import Position, PositionItem


class PositionAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'img',)

class PositionItemAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'lang', 'audio', 'position',)


admin.site.register(Position, PositionAdmin)
admin.site.register(PositionItem, PositionItemAdmin)