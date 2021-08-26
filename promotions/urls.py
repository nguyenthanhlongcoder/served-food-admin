from django.urls import path
from . import views

urlpatterns = [
    path('', views.PromotionList.as_view()),
    path('<int:pk>', views.PromotionDetail.as_view()),
]
