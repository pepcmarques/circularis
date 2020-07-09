from django.shortcuts import render  # noqa


# Create your views here.
def index(request):
    return render(request, 'index.html')