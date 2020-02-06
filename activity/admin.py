from django.contrib import admin


from activity.models import Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('description', 'img', 'state', 'date', 'lang',)
    list_filter = ('description', 'img', 'state', 'date', 'lang',)
    search_fields = ('description', 'img', 'state', 'date', 'lang',)


admin.site.register(Activity, ActivityAdmin)
