from django.urls import path

from . import views  # импортируем представления

urlpatterns = [
    path("", views.index, name="index"),
]