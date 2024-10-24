from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views , api_views
router = DefaultRouter()
router.register(r'books', api_views.BookViewSet)
router.register(r'reviews', api_views.ReviewViewSet)

urlpatterns = [
    path('api/', include((router.urls, 'api'))),
    path("api/all_books/", api_views.all_books, name="all_books"),
    path('api/class_all_books/', api_views.AllBooks.as_view(), name="class_all_books"),
    path('api/contributor_view/', api_views.ContributorView.as_view(), name="contributor_view"),
    path("books/", views.book_list, name="book_list"),
    path("books/<int:pk>/", views.book_detail, name="book_detail"),
    path("publishers/<int:pk>/", views.publisher_edit, name="publisher_edit"),
    path("publishers/new/", views.publisher_edit, name="publisher_create"),
    path("books/<int:book_pk>/reviews/new/", views.review_edit, name="review_create"),
    path(
        "books/<int:book_pk>/reviews/<int:review_pk>/",
        views.review_edit,
        name="review_edit",
    ),
    path("books/<int:pk>/media/", views.book_media, name="book_media"),
]
