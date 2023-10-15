from django.http import HttpRequest, JsonResponse

from books.models import Book


def get_all_books_json_view(request: HttpRequest) -> JsonResponse:
    all_books = Book.objects.all()

    books = []
    for one_book in all_books:
        book = {
            'id': one_book.id,
            'title': one_book.title,
            'author_full_name': one_book.author_full_name,
            'year_of_publishing': one_book.year_of_publishing,
            'copies_printed': one_book.copies_printed,
            'short_description': one_book.short_description[:45],
        }
        books.append(book)
    
    return JsonResponse(data=books, safe=False)
