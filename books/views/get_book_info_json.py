from django.http import HttpResponse, HttpRequest, JsonResponse

from books.models import Book


def get_book_info_json_view(request: HttpRequest, book_id: int) -> HttpResponse | JsonResponse:
    try:
        id = int(book_id)
    except ValueError:
        return HttpResponse(status=404)

    if id > 0:
        book = Book.objects.filter(pk=id).first()
        if book is not None:
            return JsonResponse(
                {
                'id': book.id,
                'title': book.title,
                'author_full_name': book.author_full_name,
                'year_of_publishing': book.year_of_publishing,
                'copies_printed': book.copies_printed,
                'short_description': book.short_description,
            }
            )

    return HttpResponse(status=404)