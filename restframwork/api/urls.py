from django.urls import path

from api import views

# application urls
urlpatterns = [
    path("order/", views.OrderCreate.as_view()),
    path("order/<int:pk>/", views.OrderDeatil.as_view()),
    path("orderlist/", views.OrderListView.as_view()),
    path("orderdelete/<int:pk>", views.Orderdelete.as_view()),
]
