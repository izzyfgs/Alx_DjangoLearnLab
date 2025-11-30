from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes all fields of Book.
    Includes validation to ensure publication_year is not in the future.
    """
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author and nested books using BookSerializer.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
