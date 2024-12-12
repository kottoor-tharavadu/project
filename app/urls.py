from django.urls import path
from . import views

urlpatterns = [  # Corrected variable name
    path("", views.index, name="index"),  # Define your index view properly
]
