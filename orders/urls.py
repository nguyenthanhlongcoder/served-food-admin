from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrdertList.as_view()),
    path('<int:pk>', views.OrderDetail.as_view()),
    path('order_items', views.OrderItemList.as_view()),
    path('order_items/<int:pk>', views.OrderItemDetail.as_view()),
    path('create_order', views.OrderCreateList.as_view()),
    path('create_order/<int:pk>', views.OrderCreateDetail.as_view()),
    path('create_order_item', views.OrderItemCreateList.as_view()),
    path('create_order_item/<int:pk>', views.OrderItemCreateDetail.as_view())

]
