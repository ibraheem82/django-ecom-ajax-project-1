from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    product_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)


class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)