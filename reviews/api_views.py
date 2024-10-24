from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Book, Contributor
from .serializers import BookSerializer, ContributorSerializer

@api_view()
def all_books(request):
    books = Book.objects.all()
    books_serializer = BookSerializer(books, many=True)
    return Response(books_serializer.data)


class AllBooks(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ContributorView(generics.ListAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer



