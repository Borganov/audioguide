from django.contrib import admin

# Register your models here.
from .models import Position, PositionItem

admin.site.register(Position)
admin.site.register(PositionItem)
