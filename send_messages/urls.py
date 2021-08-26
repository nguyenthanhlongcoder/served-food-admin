from django.urls import path
from . import views

urlpatterns = [
    path('', views.SendMessageList.as_view()),
    path('<int:pk>', views.SendMessageList.as_view()),
]
