from django.contrib import admin

from circularis.books.models import Book, BookStatus, BookCategory

admin.site.register(Book)
admin.site.register(BookCategory)
admin.site.register(BookStatus)
