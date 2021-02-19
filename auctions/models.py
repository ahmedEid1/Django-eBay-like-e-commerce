from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=100)


class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="listing/images", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="listings")


class Bid(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)