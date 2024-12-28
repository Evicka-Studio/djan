from django.contrib import admin
from django.urls import path
from pastes.views import create_paste, view_paste

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", create_paste, name="create_paste"),
    path("paste/<uuid:paste_id>/", view_paste, name="view_paste"),
]
