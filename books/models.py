from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    year = models.IntegerField()
    author = models.ForeignKey(
        "authors.Autor", on_delete=models.CASCADE, related_name="books"
    )
