from django.urls import path
from .views import register_view, login_view, logout_view, home_view, home_or_login
from chinh_project01.book.views import book_list

urlpatterns = [
    path('', home_or_login, name='home_or_login'), 
    path('home/', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('book/', book_list, name='book'),
]
