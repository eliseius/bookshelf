from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from books.models import Book


def get_book_info_view(request: HttpRequest, book_id: int) -> HttpResponse:
    if book_id > 0:
        book = Book.objects.filter(pk=book_id).first()
        if book is not None:
            return render (request, 'book_info.html', context={"book": book})
    return HttpResponse(status=404)
