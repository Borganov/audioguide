from django.contrib import admin

# Register your models here.
from .models import Position, PositionItem


class PositionAdmin(admin.ModelAdmin):
    list_display = ('lang', 'name', 'order', 'state', )
    list_filter = ('order', 'name', 'state', )
    search_fields = ('order', 'name', 'state', )
    list_editable = ('name', 'order', 'state', )


class PositionItemAdmin(admin.ModelAdmin):
    list_display = ('lang','position', 'order','img', 'titre', 'description', 'audio', 'state',  )
    list_filter = ('titre', 'description', 'lang', 'audio', 'position','img','order', 'state', )
    search_fields = ('titre', 'description', 'lang', 'audio', 'position','img','order', 'state', )
    list_editable = ('titre', 'description', 'audio', 'position','img','order', 'state', )


admin.site.register(Position, PositionAdmin)

admin.site.register(PositionItem, PositionItemAdmin)
