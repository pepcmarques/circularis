from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse

from circularis.books.forms import CreateBook, SearchIsbnForm
from circularis.books.models import Book


def image(request):
    image_file = request.FILES['image_file'].file.read()
    Book.objects.create(image=image_file)


@login_required()
def list_books(request, book_list):
    paginator = Paginator(book_list, 25)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books.html', {'page_obj': page_obj})


@login_required()
def list_all_books(request):
    book_list = Book.objects.get_books()
    return list_books(request, book_list)


@login_required()
def list_my_books(request):
    book_list = Book.objects.get_books_by_user(user=request.user)
    return list_books(request, book_list)


@login_required()
def add_book(request):
    if request.method == 'POST':
        form = CreateBook(request.POST)
        if form.save():
            return redirect(reverse('base:home'))
    else:
        form = CreateBook()
    return render(request, 'book.html', {'form': form})


@login_required()
def update_book(request, pk):
    if request.method == 'POST':
        form = CreateBook(request.POST)
        if form.is_valid():
            if form.save(request.user):
                return redirect(reverse('base:home'))
    else:
        book_instance = Book.objects.get_books(user=request.user, pk=pk)
        form = CreateBook(instance=book_instance)
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
