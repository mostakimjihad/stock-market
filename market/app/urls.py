from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("add", views.add, name="add" ),
    path("edit", views.edit, name="edit"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("update/<int:id>", views.update, name="update"),
    path("doupdate/<int:id>", views.doupdate, name="doupdate")
]