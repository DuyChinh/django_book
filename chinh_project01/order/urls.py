from django.urls import path
from chinh_project01.order.views import create_order, order_detail, order_list

urlpatterns = [
    path('create_order/', create_order, name='create_order'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
    path('orders/', order_list, name='order_list'),
]
