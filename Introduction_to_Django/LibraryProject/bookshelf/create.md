\# Retrieve Book



from bookshelf.models import Book



\# Retrieve the book we created by ID

book = Book.objects.get(id=1)

book

\# Expected output: <Book: 1984 by George Orwell (1949)>



