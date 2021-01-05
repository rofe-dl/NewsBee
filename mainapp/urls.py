from django.urls import path

from . import views

app_name = "mainapp"

urlpatterns = [
    path("news", views.index, name="news"),
    path("mycollection", views.my_collection_view, name="my_collection"),
    path("share", views.share_view, name="share"),
    path("delete", views.delete_view, name="delete"),
    path("beenews", views.bee_news_view, name="bee_news"),
    path("news/search/", views.search_news_view, name="search_news"),
    path("mycollection/search/", views.search_my_collection_view, name="search_my_collection")
]