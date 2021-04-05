from circularis.base.models import Address
from circularis.books.models import Book, BookStatus


def clean_isbn(isbn):
    return ''.join([s for s in isbn if s.isdigit()])


def is_possible_isbn(isbn):
    isbn = clean_isbn(isbn)
    return len(isbn) == 10 or len(isbn) == 13


def validate_isbn(isbn):
    isbn = clean_isbn(isbn)
    return is_possible_isbn(isbn) or len(isbn) == 0


def search_for_book(isbn):
    return {"title": "This is a book",
            "isbn10": isbn if len(isbn) == 10 else "",
            "isbn13": isbn if len(isbn) == 13 else ""
            }


def pre_populate_book_form(user):
    book = Book()
    book.address = Address.objects.get_address_or_none_by_user(user)
    book.user = user
    book.status = BookStatus.objects.get(code=BookStatus.BookStatusChoices.AV)
    return book
