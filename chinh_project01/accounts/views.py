from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from chinh_project01.book.models import Book

def home_or_login(request):
    if request.user.is_authenticated:  
        return redirect('book')  
    else:
        return redirect('login')

@login_required
def home_view(request):
    return render(request, "accounts/home.html", {"user": request.user})

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, "book/book_list.html", {"books": books})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book')  
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')  

