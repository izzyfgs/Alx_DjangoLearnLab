\# Update Book



\# Update the book's title

book.title = "Nineteen Eighty-Four"

book.save()



\# Check update

Book.objects.get(id=book.id)

\# <Book: Nineteen Eighty-Four by George Orwell (1949)>



