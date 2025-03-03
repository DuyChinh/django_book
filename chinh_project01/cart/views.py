from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart
from chinh_project01.book.models import Book
from chinh_project01.order.models import Order

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart_view')

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, book=book)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, "cart/cart.html", {"cart_items": cart_items})


# @login_required
# def create_order(request):
#     # Lấy các mục trong giỏ hàng của người dùng
#     cart_items = Cart.objects.filter(user=request.user)
    
#     # Kiểm tra nếu giỏ hàng trống
#     if not cart_items:
#         return redirect('cart_view')  # Chuyển hướng về giỏ hàng nếu không có sản phẩm

#     selected_items = request.POST.getlist('selected_items')
    
#     if not selected_items:
#         return redirect('cart_view')  # Nếu không có sản phẩm nào được chọn
    
#     total_price = 0
#     order = Order.objects.create(user=request.user)
    
#     # Tính tổng tiền cho các sản phẩm đã chọn
#     for item_data in selected_items:
#         item_id, item_price = item_data.split('_')
#         total_price += float(item_price)

#     order.total_price = total_price
#     order.save()
    
#     # Xóa các mục đã được chọn từ giỏ hàng
#     Cart.objects.filter(id__in=[item.split('_')[0] for item in selected_items]).delete()
    
#     return redirect('order_detail', order_id=order.id)
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
