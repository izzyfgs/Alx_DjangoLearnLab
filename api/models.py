from django.db import models  # Make sure this import is at the top


# Author model: represents a writer who can have many books
class Author(models.Model):
    # Stores the name of the author
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model: represents a book written by an Author
# Demonstrates a one-to-many relationship (one Author → many Books)
class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=255)

    # Year the book was published
    publication_year = models.IntegerField()

    # ForeignKey establishes the one-to-many relationship
    author = models.ForeignKey(
        Author,
        related_name="books",  # Allows nested serialization via author.books
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"



# Create your models here.
