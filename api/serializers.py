from rest_framework import serializers
from .models import Author, Book
import datetime

# Defines the BookSerializer, which serializes Book model instances.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Validates that the publication_year is not in the future.
    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Defines the AuthorSerializer, which serializes Author model instances, including nested books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
