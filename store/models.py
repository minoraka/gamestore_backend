from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 


class Platform(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name 


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 


class Game(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="games/", blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    platform = models.ManyToManyField(Platform)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 


class Discount(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    percent = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name 


class DLC(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name 


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name 