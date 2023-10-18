from django.contrib import admin
from django.urls import path

from books.views.show_all_books_html import show_all_books_html_view
from books.views.get_book_info import get_book_info_view
from books.views.get_all_books_json import get_all_books_json_view
from books.views.get_book_info_json import get_book_info_json_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', show_all_books_html_view),
    path('books/<int:book_id>/', get_book_info_view),
    path('api/books/', get_all_books_json_view),
    path('api/books/<int:book_id>/', get_book_info_json_view)
]
