"""circularis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from circularis.books import views

app_name = 'books'

urlpatterns = [
    path('', views.add_book, name="add_book"),
    path('all/', views.list_all_not_my_books, name="all_books"),
    path('my/', views.list_my_books, name="my_books"),
    path('request/<int:pk>', views.request_book, name="request"),
    path('<int:pk>', views.update_book, name="update_book"),
]
