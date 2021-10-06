from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from circularis.base.decorators import require_address
from circularis.base.models import Address
from circularis.books.forms import CreateBook, SearchIsbnForm, UpdateBook
from circularis.books.models import Book, BookStatus
from circularis.messaging.models import MessageOneOne
from circularis.messaging.services import process_book_request, process_book_reject_request, process_delete_message, \
    process_accept_request


def image(request):
    image_file = request.FILES['image_file'].file.read()
    Book.objects.create(image=image_file)


@login_required()
def list_books(request, book_list, place="all"):
    paginator = Paginator(book_list, 25)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if place == "all":
        return render(request, 'books.html', {'page_obj': page_obj})
    elif place == "my":
        return render(request, 'my_books.html', {'page_obj': page_obj})


@login_required()
def list_all_not_my_books(request):
    book_list = Book.objects.get_books_by_not_user(user=request.user)
    return list_books(request, book_list, "all")


@login_required()
def list_my_books(request):
    book_list = Book.objects.get_books_by_user(user=request.user)
    return list_books(request, book_list, "my")


@login_required()
def add_book(request):
    if request.method == 'POST':
        form = CreateBook(request.POST, request.FILES)
        if form.is_valid():
            new_book = form.save(commit=False)
            address = Address.objects.get(user=request.user)
            if address is None:
                return redirect(reverse('base:update_address'))
            new_book.user = request.user
            new_book.address = address
            new_book.status = BookStatus.objects.get(code=BookStatus.BookStatusChoices.AV)  # This is the default.
            new_book.save()
            return redirect(reverse('base:home'))
    else:
        form = CreateBook()
    return render(request, 'book.html', {'form': form})


@login_required()
def update_book(request, pk):
    if request.method == 'POST':
        obj = get_object_or_404(Book, id=pk)
        form = UpdateBook(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            book = form.save(commit=False)
            # TODO: Status = checked out

            address = Address.objects.get(user=request.user)
            if address is None:
                return redirect(reverse('base:update_address'))
            book.user = request.user
            book.address = address

            book.save()
            return redirect(reverse('books:my_books'))
    else:
        book_instance = Book.objects.get(pk=pk)
        if book_instance.user != request.user:
            return redirect(reverse('books:my_books'))
        form = UpdateBook(instance=book_instance)
    return render(request, 'book.html', {'form': form})


@login_required()
def add_by_isbn(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchIsbnForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            #
            # book = search_for_book(request.data.cleaned_data['isbn'])
            #
            # redirect to a new URL:
            return redirect(reverse('books:add_book'))  # how to pass data ????
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchIsbnForm()

    return render(request, 'add_by_isbn.html', {'form': form})


@login_required()
@require_address()
def request_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.user == book.user:
        messages.add_message(request, messages.INFO, "Sorry, but you can't request a book that it is with you")
        return redirect(reverse('books:all_books'))

    if request.method == 'POST':
        if process_book_request(request, book):
            messages.add_message(request, messages.INFO, "Book request message was sent")
        else:
            messages.add_message(request, messages.ERROR, "Couldn't process the book request")
        return redirect(reverse('books:all_books'))

    return render(request, 'request_confirm.html')


@login_required()
@require_address()
def reject_request_book(request, pk):
    message = MessageOneOne.objects.get(pk=pk)

    if request.method == 'POST':
        if process_book_reject_request(request, message):
            messages.add_message(request, messages.INFO, "Reject book request message was sent")
        else:
            messages.add_message(request, messages.ERROR, "Couldn't process the book reject")
        return redirect(reverse('messaging:my_messages'))

    return render(request, 'reject_confirm.html')


@login_required()
@require_address()
def delete_request_book(request, pk):
    message = MessageOneOne.objects.get(pk=pk)

    if request.method == 'POST':
        if process_delete_message(request, message):
            messages.add_message(request, messages.INFO, "Delete book request")
        else:
            messages.add_message(request, messages.ERROR, "Couldn't process the book reject")
        return redirect(reverse('messaging:my_messages'))

    return render(request, 'delete_confirm.html')


@login_required()
@require_address()
def accept_request_book(request, pk):
    message = MessageOneOne.objects.get(pk=pk)

    if request.method == 'POST':
        if process_accept_request(request, message):
            messages.add_message(request, messages.INFO, "Accept book request message was sent")
        else:
            messages.add_message(request, messages.ERROR, "Couldn't process the book request (accept)")
        return redirect(reverse('messaging:my_messages'))

    return render(request, 'accept_confirm.html')
