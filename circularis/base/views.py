from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from circularis.base.forms import CreateAddress
from circularis.base.models import Address


def index(request):
    return render(request, 'index.html', {'user': request.user, })


@login_required()
def home(request):
    if not Address.objects.has_address(request.user):
        return render(request, 'config_home.html', {'system_name': settings.SYSTEM_NAME, 'welcome': True})
    # if len(Book.objects.get_books_by_user(request.user)) == 0:
    #    return redirect('books:my_books')
    return redirect('books:all_books')


@login_required()
def update_address(request):
    if request.method == 'POST':
        form = CreateAddress(request.POST)
        if form.save(request.user):
            return redirect(reverse('base:home'))
    else:
        address_instance = Address.objects.get_address_or_none_by_user(request.user)
        form = CreateAddress(instance=address_instance)
    return render(request, 'address.html', {'form': form})


def default_map(request):
    return render(request, 'maps.html',
                  {'mapbox_access_token': settings.MAPBOX_ACCESS_KEY})
