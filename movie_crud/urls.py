from django.urls import path
from . import views

app_name = "movie_crud"
urlpatterns = [
    path("", views.main, name="main"),
    path("index/", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
]
