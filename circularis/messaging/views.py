from django.contrib import messages
from django.urls import reverse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from circularis.messaging.models import MessageOneOne
from circularis.messaging.services import process_delete_message


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


@login_required()
def delete_message(request, pk):
    message = MessageOneOne.objects.get(pk=pk)

    if request.method == 'POST':
        if process_delete_message(request, message):
            messages.add_message(request, messages.INFO, "Message deleted")
        else:
            messages.add_message(request, messages.ERROR, "Couldn't process the message deletion")
        return redirect(reverse('messaging:my_messages'))

    return render(request, 'delete_msg_confirm.html')
