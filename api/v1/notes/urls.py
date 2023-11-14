from django.urls import re_path

from api.v1.notes import views

app_name = "api_v1_notes"

urlpatterns = [
    re_path(r'^add-notes/$', views.add_notes, name="add-notes"),
    re_path(r'^list-notes/$', views.list_notes, name="list-notes"),
    re_path(r'^single-note/(?P<pk>.*)/$', views.single_note, name="single-notes"),
    re_path(r'^edit-note/(?P<pk>.*)/$', views.edit_note, name="edit-notes"),
    re_path(r'^delete-note/(?P<pk>.*)/$', views.delete_note, name="delete-notes"),

]