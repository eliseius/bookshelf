from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from books.models import Book


def show_all_books_html_view(request: HttpRequest) -> HttpResponse:
    all_books = Book.objects.all()

    return render(request, 'all_books.html', context={"all_books": all_books})
