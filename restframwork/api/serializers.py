from rest_framework import serializers

from .models import Order


# form created  Order add data
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "name", "email", "address")
