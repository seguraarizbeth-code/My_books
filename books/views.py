from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})


def detail_book(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/detail_book.html', {'book': book})


def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/detail_book.html', {'book': book})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('home')


def add_book(request):
    return redirect('home')