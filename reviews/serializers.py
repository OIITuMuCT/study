from rest_framework import serializers

from .models import Book, Publisher, Contributor, BookContributor

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
