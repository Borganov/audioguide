from django.contrib import admin


from activity.models import Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('lang','number', 'description', 'img', 'state', 'date','site', )
    list_filter = ('number', 'description', 'img', 'state', 'date', 'lang', 'site', )
    search_fields = ('description', 'img', 'state', 'date', 'lang', 'site', )
    list_editable = ('img', 'state','description', 'number', 'site', )


admin.site.register(Activity, ActivityAdmin)
