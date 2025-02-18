from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from chinh_project01.cart.models import Cart

def book_list(request):
    books = Book.objects.all()
    carts = Cart.objects.all()
    return render(request, "book/book_list.html", {"books": books, "num_cart": len(carts)})

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
