from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated, PermissionDenied

from .models import Book, Publisher, Contributor, BookContributor, Review
from .utils import average_rating

# Version view ModelSerializer
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'website', 'email']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'isbn', 'publisher']


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookContributor
        fields = ['book', 'contributor', 'role']


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['first_names', 'last_names', 'email']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['book','content', 'rating', 'date_created', 'creator', ]


# Version view Serializer
# class PublisherSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     website = serializers.URLField()
#     email = serializers.EmailField()


# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     publication_date = serializers.DateField()
#     isbn = serializers.CharField()
#     publisher = PublisherSerializer()

# ? разобраться с этим 
# class UserViewSet(viewsets.ModelViewSet):
#     serializers_class = UserSerializer
#     queryset = User