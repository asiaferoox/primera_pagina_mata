from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('crear/autor/', views.crear_autor, name='crear_autor'),
    path('crear/categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear/libro/', views.crear_libro, name='crear_libro'),
    path('buscar/', views.buscar_libro, name='buscar_libro'),
]
