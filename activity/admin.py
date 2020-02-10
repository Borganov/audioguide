from django.contrib import admin


from activity.models import Activity, Language


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('lang','number', 'description', 'img', 'isActive', 'date', )
    list_filter = ('number', 'description', 'img', 'isActive', 'date', 'lang',  )
    search_fields = ('description', 'img', 'isActive', 'date', 'lang', )
    list_editable = ('img', 'isActive','description', 'number',  )

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('designation','img', 'isActive',)
    list_filter = ('designation','img', 'isActive', )
    search_fields = ('designation','img', 'isActive',)
    list_editable = ('img', 'isActive', )


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Language, LanguageAdmin)
