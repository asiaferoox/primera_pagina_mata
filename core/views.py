
from django.shortcuts import render, redirect
from .models import Libro
from .forms import AutorForm, CategoriaForm, LibroForm

# Create your views here.
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

def crear_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'crear_objeto.html', {'form': form, 'titulo': 'Crear Autor'})

def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'crear_objeto.html', {'form': form, 'titulo': 'Crear Categoría'})

def crear_libro(request):
    form = LibroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'crear_objeto.html', {'form': form, 'titulo': 'Crear Libro'})

def buscar_libro(request):
    q = request.GET.get('q', '')
    resultados = Libro.objects.filter(titulo__icontains=q) if q else []
    return render(request, 'buscar_libro.html', {'resultados': resultados, 'query': q})
