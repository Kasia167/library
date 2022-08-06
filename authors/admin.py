from django.contrib import admin

# Register your models here.
from authors.models import Autor


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    pass
