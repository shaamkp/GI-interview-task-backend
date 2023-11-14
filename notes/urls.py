
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "GI Interview Task Notes Admin"
admin.site.site_title = "GI Interview Task Notes Admin"
admin.site.index_title = "Welcome to GI Interview Task Notes Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/notes/', include('api.v1.notes.urls', namespace='api_v1_notes')),
]
