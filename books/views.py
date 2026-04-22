from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})


def detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/detail.html', {'book': book})


