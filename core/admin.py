from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Autor, Categoria, Libro

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Libro)
