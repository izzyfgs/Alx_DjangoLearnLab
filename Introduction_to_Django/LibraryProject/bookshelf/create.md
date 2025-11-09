\# Create Book



from bookshelf.models import Book



\# Create a Book instance

book = Book.objects.create(title="1984", author="George Orwell", publication\_year=1949)

book

\# <Book: 1984 by George Orwell (1949)>



