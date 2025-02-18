from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required

# Hiển thị danh sách sách
def book_list(request):
    books = Book.objects.all()
    return render(request, "book/book_list.html", {"books": books})

# Thêm sách mới
@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, "book/add_book.html", {"form": form})
