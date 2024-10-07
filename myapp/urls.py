from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome_view, name="welcome_view"),
    path("books/", views.book_list, name="book_list"),
    path("polls/", views.survey, name="polls"),
    path("book-search", views.book_search),
    path("home-page/", views.HomePage.as_view(), name="home_page"),
    path("index/", views.index, name='index'),
]
