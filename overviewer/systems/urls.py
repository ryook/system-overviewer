from django.views.generic import TemplateView
from django.urls import path

from . import views


app_name = "systems"
urlpatterns = [
    path("api/v1/systems", views.SystemAPIView.as_view()),
    path("", TemplateView.as_view(template_name="systems/index.html"))
]
