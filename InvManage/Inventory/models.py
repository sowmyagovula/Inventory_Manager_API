from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.utils import timezone

# Create your models here.
class Inventory_model(models.Model):
    CATEGORY_CHOICES = [
        ('Fashion', 'Fashion'),
        ('Electronics', 'Electronics'),
        ('Food & Beverage', 'Food & Beverage'),
        ('Home Goods', 'Home Goods'),
        ('Books', 'Books'),
        ('Toys & Games', 'Toys & Games'),
        ('Sporting Goods', 'Sporting Goods'),
        ('Health & Beauty', 'Health & Beauty'),
        ('Automotive', 'automotive'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Fashion',
    )
    product_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0,validators=[MaxValueValidator(100)])
    image = models.ImageField(upload_to='media/', blank=False, null = False)

    def __str__(self):
        return f"{self.user.username} - {self.product_name} - {self.price} - {self.stock}"

