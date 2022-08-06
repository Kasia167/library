from django.db import models


# Create your models here.
class Autor(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    wiek = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
