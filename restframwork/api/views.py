from rest_framework import generics

from .models import Order
from .serializers import OrderSerializer

# serializer used for complex data to native python data convert


class OrderCreate(generics.CreateAPIView):
    # order create api
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDeatil(generics.RetrieveUpdateDestroyAPIView):
    # order deatil (upadte) api  as pk (key)  pass in urls
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListView(generics.ListAPIView):
    # all order view api
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class Orderdelete(generics.DestroyAPIView):
    # order delete api , pk (key=id) pass on url
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
