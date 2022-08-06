from django.shortcuts import render

# Create your views here.
from authors.models import Autor


def details(request, author_id):
    author = Autor.objects.get(pk=author_id)

    context = {"author": author}
    return render(request, "authors/details.html", context)


def list(request):
    authors = Autor.objects.all()

    context = {"authors": authors}
    return render(request, "authors/list.html", context)
