from django.urls import path

from .views import (
    BookRecordFormView,
    FormSuccessView,
    FormDeleteSuccessView,
    BookCreateView,
    BookRecordDetailView,
    BookRecordListView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path("new_book_record", BookRecordFormView.as_view(), name="book_record_form"),
    path("entry_success", FormSuccessView.as_view(), name="form_success"),
    path('delete_success', FormDeleteSuccessView.as_view(), name='form_delete_success'),
    path('', BookRecordListView.as_view(), name='book_record_list'),
    path("book_record_create", BookCreateView.as_view(), name="book_create"),
    path(
        "book_record_detail/<int:pk>",
        BookRecordDetailView.as_view(),
        name="book_detail",
    ),
    path("book_record_update/<int:pk>", BookUpdateView.as_view(), name="book_update"),
    path("book_record_delete/<int:pk>", BookDeleteView.as_view(), name="book_delete"),
    
]
