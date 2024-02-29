from django.http import HttpResponse, HttpRequest, JsonResponse
from django.core import serializers
from books.models import Book


def get_book_info_json_view(request: HttpRequest, book_id: int) -> HttpResponse:# | JsonResponse:
    if book_id > 0:
        book = Book.objects.filter(pk=book_id)
        if book:
            data = serializers.serialize("json", book)
            return HttpResponse(data)
    return HttpResponse(status=404)
