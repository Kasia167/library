from django.shortcuts import render

# Create your views here.
from books.models import Book


def details(request, book_id):
    book = Book.objects.get(pk=book_id)

    context = {"book": book}
    return render(request, "books/details.html", context)


def list(request):
    books = Book.objects.all()

    context = {"books": books}
    return render(request, "books/list.html", context)
