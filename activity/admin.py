from django.contrib import admin

from activity.models import Activity, Language, ActivityItem


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('date', 'number','title', 'prestataire', 'img', 'isActive',  )
    list_filter = ('number', 'isActive', 'date','title','prestataire',)
    search_fields = ('isActive', 'date','title','prestataire',)
    list_editable = ('isActive', 'number', 'img', 'title','prestataire',)


class ActivityItemAdmin(admin.ModelAdmin):
    list_display = ('lang', 'activity', 'order', 'title', 'description',  'isActive')
    list_filter = ('title', 'order', 'description', 'activity', 'lang', 'isActive')
    search_fields = ('title', 'order', 'description', 'activity', 'lang', 'isActive')
    list_editable = ('title', 'order', 'description', 'activity', 'isActive')


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('abreviation', 'designation', 'img', 'imgMouse', 'isActive',)
    list_filter = ('abreviation', 'designation', 'img', 'imgMouse', 'isActive',)
    search_fields = ('abreviation', 'designation', 'img','imgMouse',  'isActive',)
    list_editable = ('designation', 'img', 'imgMouse', 'isActive',)


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(ActivityItem, ActivityItemAdmin)
