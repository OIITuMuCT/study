from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .models import Book
from .serializers import BookSerializer

@api_view()
def all_books(request):
    books = Book.objects.all()
    books_serializer = BookSerializer(books, many=True)
    return Response(books_serializer.data)


class AllBooks(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer