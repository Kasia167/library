from django.urls import path
from .views import dashboard, example_view


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("examples/formform", example_view, name="example_view"),
]
