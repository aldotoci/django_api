from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name="index"),
    path('category/', views.category, name="category"),
    path('watch/', views.watch, name="watch"),
    path('genre/', views.genre, name="genre"),
    path('recent/', views.recent, name="recent")
]