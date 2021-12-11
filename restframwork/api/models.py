from django.db import models


class Order(models.Model):
    # order model created self
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    address = models.TextField(max_length=200)
