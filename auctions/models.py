from turtle import title
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

#Define the listing model
class Listing(models.Model):
    title = models.CharField(max_length=64)
    image = models.URLField()
    # condition field intended to hold items
    # from a drop down with 4 options
    # new, excellent, good, as described
    condition = models.CharField(max_length=12)
    description = models.TextField()
    startPrice = models.DecimalField(decimal_places=2, max_digits=4)
    currentPrice = models.DecimalField(decimal_places=2, max_digits=4)
    # duration field intended to hold items
    # from a drop down with 3 options 
    # 1 day, 7 days, 10 days
    duration = models.CharField(max_length=12) 
    remainingTime = models.DurationField()
    listDate = models.DateTimeField()

    def __str__(self):
        return f"Auction {self.id}: {self.title}, condition {self.condition}"




#class Bid

#class Comment