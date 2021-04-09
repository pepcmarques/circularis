from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

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


def to_thumbnail(image):
    max_size = (100, 100)

    # Convert from InMemoryUploadedFile to Image (PIL)
    im_pic = Image.open(image)
    im_pic.thumbnail(max_size)

    pic_io = BytesIO()
    im_pic.save(pic_io, im_pic.format)

    image.content_type = f"image/{im_pic.format.lower()}"

    # Convert back
    pic_file = InMemoryUploadedFile(
        file=pic_io,
        field_name=None,
        name=image.name,
        content_type=image.content_type,
        size=image.size,
        charset=None
    )

    return pic_file
