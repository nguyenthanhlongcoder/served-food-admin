from django.urls import path
from . import views

urlpatterns = [
    path('', views.FCMDeviceList.as_view()),
    path('<int:pk>', views.FCMDeviceDetail.as_view()),

]
