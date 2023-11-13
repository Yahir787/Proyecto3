from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/profile/", views.index, name="index"),
    path("artwork/<int:artwork_id>", views.artwork, name="artwork"),
    path("artwork/<int:artwork_id>/add", views.artwork_add_to_collectionFORM, name="artwork_collection"),
    path("artwork/<int:artwork_id>/add/<int:collection_id>", views.SendArtworkTo, name="artwork_collection"),
    path("artworks/search", views.search_artworks, name="search_artworks"),
    path("accounts/register/", views.register, name="register"),
    path("collections/", views.collections, name="collections"),
    path("collection_list/", views.collection_list, name="collection_list"),
    path("collection/add", views.collection_add, name="collection_add"),
    path('collection/<int:collection_id>/edit/', views.collection_edit, name='collection_edit'),
    path('collection/<int:collection_id>/delete', views.collection_delete, name='collection_delete'),
    path('collection/<int:collection_id>', views.collection_artworks, name='colection artworks')
]
