from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrdertList.as_view()),
    path('<int:pk>', views.OrderDetail.as_view()),
    path('order_item', views.OrderItemList.as_view()),
    path('order_item/<int:pk>', views.OrderItemDetail.as_view()),

]
