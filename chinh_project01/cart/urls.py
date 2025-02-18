from django.urls import path
from .views import add_to_cart, cart_view, remove_from_cart

urlpatterns = [
    path('add/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('', cart_view, name='cart_view'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),  
]

