from django.urls import path

from . import views


app_name = "systems"
urlpatterns = [
    path("api/system", views.SystemView.as_view())
]