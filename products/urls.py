from django.urls import path
from django.urls.conf import re_path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('<int:pk>', views.ProductDetail.as_view()),
    path('variation', views.VariationList.as_view()),
    path('variation/<int:pk>', views.VariationDetail.as_view()),
    path('label', views.LabelList.as_view()),
    path('label/<int:pk>', views.LabelDetail.as_view()),
]
