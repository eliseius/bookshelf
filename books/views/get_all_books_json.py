from django.http import HttpRequest, HttpResponse
from django.core import serializers

from books.models import Book


def get_all_books_json_view(request: HttpRequest) -> HttpResponse:
    data = serializers.serialize("json", Book.objects.all())
    return HttpResponse(data)
