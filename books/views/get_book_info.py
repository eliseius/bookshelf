from django.http import HttpResponse, HttpRequest

from books.models import Book


def get_book_info_view(request: HttpRequest, book_id: int) -> HttpResponse:
    try:
        id = int(book_id)
    except ValueError:
        return HttpResponse(status=404)

    if id > 0:
        book = Book.objects.filter(pk=id).first()
        if book is not None:
            return HttpResponse(book)
    return HttpResponse(status=404)
