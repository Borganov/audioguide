from django.contrib import admin

# Register your models here.
from activity.models import Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('description', 'img', 'state', 'date', 'lang',)


admin.site.register(Activity, ActivityAdmin)
