from django.contrib import admin

from . models import Notes


class NotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body')

admin.site.register(Notes, NotesAdmin)
