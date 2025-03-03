from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order
from chinh_project01.cart.models import Cart
from chinh_project01.book.models import Book

@login_required
def create_order(request):
    selected_items = request.POST.getlist('selected_items')
    print("=====================================")
    print("selected items: ", selected_items)

    if not selected_items:
        return redirect('cart_view')  

    order = Order.objects.create(user=request.user, total_price=0)

    total_price = 0
    cart_items = []

    for item_data in selected_items:
        item_id, item_price = item_data.split('_')
        item_price = item_price.replace(',', '') 

        # Lấy sản phẩm từ giỏ hàng
        cart_item = get_object_or_404(Cart, id=item_id)
        cart_items.append(cart_item)
        
        # Tính tổng giá
        total_price += int(item_price) 
    print(total_price)

    # Gán tổng tiền cho đơn hàng
    order.total_price = total_price
    order.save()

    # Thêm sản phẩm vào đơn hàng
    for cart_item in cart_items:
        order.cart_items.add(cart_item)

    order.save()
    orders = Order.objects.all()
    print("orders: ", orders)

    # Xóa các sản phẩm đã đặt khỏi giỏ hàng
    # Cart.objects.filter(id__in=[item.split('_')[0] for item in selected_items]).delete()

    return redirect('order_detail', order_id=order.id)

@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    cart_items = order.cart_items.all()
    # print("cart items: ",cart_items, type(cart_items))
    books = []
    for item in cart_items.all():
        # print("item: ",item.book)
        book = Book.objects.get(id=item.book.id)
        books.append(book)

    return render(request, 'order/order_detail.html', {'order': order, 'cart_items': cart_items, 'books': books})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    print(len(orders))
    order_data = []
    for order in orders:
        books = [cart_item.book for cart_item in order.cart_items.all()]
        order_data.append({
            'order': order,
            'books': books
        })

    return render(request, 'order/order_list.html', {'order_data': order_data})
