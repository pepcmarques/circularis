from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from circularis.messaging.models import MessageOneOne


@login_required()
def list_books(request, book_list):
    paginator = Paginator(book_list, 25)  # Show 25 messages per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'my_messages.html', {'page_obj': page_obj})


@login_required()
def list_my_messages(request):
    message_list = MessageOneOne.objects.filter(receiver=request.user)
    return list_books(request, message_list)
