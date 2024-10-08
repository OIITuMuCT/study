from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome_view, name="welcome_view"),
    path("books/", views.book_list, name="book_list"),
    path("books/<int:pk>/", views.book_detail, name='book_detail'),
    path("polls/", views.survey, name="polls"),
    path("home-page/", views.HomePage.as_view(), name="home_page"),
    path("index/", views.index, name='index'),
]
