from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)


class Receipt(models.Model):
    cartitems = models.ManyToManyField('CartItem')
    date = models.DateField()
    loyalty_id = models.IntegerField()
    receipt_id = models.IntegerField()
    turnover = models.FloatField(default=0)


class CartItem(models.Model):
    name = models.CharField(max_length=255)



