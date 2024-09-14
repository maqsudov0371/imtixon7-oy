from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    phone = models.CharField(max_length=13, db_index=True)

    def __str__(self) -> str:
        return f"{self.username}"
    

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    oldprice = models.DecimalField(max_digits=10, decimal_places=2)
    about_products = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/products/', help_text="O'lcham:  470x416 px")
    image1 = models.ImageField(upload_to='media/products/detail/', help_text="O'lcham:  149x118 px", unique=True, blank=True)
    image2 = models.ImageField(upload_to='media/products/detail/', help_text="O'lcham:  149x118 px", unique=True, blank=True)
    image3 = models.ImageField(upload_to='media/products/detail/', help_text="O'lcham:  149x118 px", unique=True, blank=True)
    image4 = models.ImageField(upload_to='media/products/detail/', help_text="O'lcham:  149x118 px", unique=True, blank=True)

    def __str__(self) -> str:
        return self.name


class ForFooter(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=50)
    image = models.ImageField(upload_to='media/footer', help_text="O'lcham:  658x543 px")
    bigimage = models.ImageField(upload_to='media/footer')
    miniimage1 = models.ImageField(upload_to='media/minifooter', help_text="O'lcham: 90x90 px")
    miniimage2 = models.ImageField(upload_to='media/minifooter', help_text="O'lcham: 115x96 px")
    miniimage3 = models.ImageField(upload_to='media/minifooter', help_text="O'lcham: 115x96 px")
    miniimage4 = models.ImageField(upload_to='media/minifooter', help_text="O'lcham: 60x66 px")
    miniimage5 = models.ImageField(upload_to='media/minifooter', help_text="O'lcham: 114x97 px")

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.product.name}'