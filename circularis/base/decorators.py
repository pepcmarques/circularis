from functools import wraps

from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

from circularis.base.models import Address


def require_address():
    def decorator(func):
        @wraps(func)
        def check_address(request, **kwargs):
            if Address.objects.has_address(request.user):
                return func(request, **kwargs)
            messages.add_message(request, messages.ERROR,
                                 "Sorry, but you can't request a book if you don't have an registered address")
            return redirect(reverse('base:update_address'))
        return check_address
    return decorator
