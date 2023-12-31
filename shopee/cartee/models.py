from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='product/image')
    product_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    
    def __str__(self):
        return self.name



class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.owner.username
    
    #  Calculating the total by summing up the subtotal attribute of each CartItem in the cartitems list. It uses a list comprehension to create a list of subtotals.
    @property
    def grandtotal(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.subtotal for item in cartitems])
        return total
    
    @property
    def cartquantity(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.quantity for item in cartitems])
        return total
        

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.name
    
    @property
    def subtotal(self):
        total = self.quantity * self.product.price    
        return total