from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.wiki, name="wiki"),
    path("search_wiki.html", views.search_wiki, name="search-wiki"),
    path("create_page.html", views.create_page, name="create-page"),
    path("already_exists.html", views.already_exists, name="already-exists"),
    path("edit_page.html", views.edit_page, name="edit-page"),
    path("random/", views.random_page, name="random-page")
]
