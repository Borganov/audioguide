from django.contrib import admin


from activity.models import Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ( 'lang','number', 'description', 'img', 'state', 'date',)
    list_filter = ('number', 'description', 'img', 'state', 'date', 'lang',)
    search_fields = ('number', 'description', 'img', 'state', 'date', 'lang',)
    list_editable = ('number', 'img', 'state', 'date', 'description')


admin.site.register(Activity, ActivityAdmin)
