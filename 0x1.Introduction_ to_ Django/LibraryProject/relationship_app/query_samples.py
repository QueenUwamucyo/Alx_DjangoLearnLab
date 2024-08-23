# Import the models
from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f'- {book.title}')
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")

# Query 2: List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"Books in {library_name}:")
        for book in books_in_library:
            print(f'- {book.title}')
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library_name}: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print(f"Either the library '{library_name}' or its librarian does not exist.")

# Sample function calls
if __name__ == "__main__":
    get_books_by_author("John Doe")
    get_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
