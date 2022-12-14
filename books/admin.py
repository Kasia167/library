from django.contrib import admin

# Register your models here.
from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "author_first_name",
        "author_last_name",
        "author_last_name",
    ]

    def author_first_name(self, obj):
        return obj.author.imie

    def author_last_name(self, obj):
        return obj.author.nazwisko

    author_first_name.admin_order_field = "author__imie"
