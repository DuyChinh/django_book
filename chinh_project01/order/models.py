from django.db import models
from django.contrib.auth.models import User
from chinh_project01.cart.models import Cart

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')
    # total_price = models.DecimalField(max_digits=10, decimal_places=2)
    cart_items = models.ManyToManyField(Cart)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username} ({self.status})"

