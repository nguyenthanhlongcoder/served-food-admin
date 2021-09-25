from django.urls import path
from django.urls.conf import re_path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('<int:pk>', views.ProductDetail.as_view()),
    path('variations', views.VariationList.as_view()),
    path('variations/<int:pk>', views.VariationDetail.as_view()),
    path('labels', views.LabelList.as_view()),
    path('labels/<int:pk>', views.LabelDetail.as_view()),
    path('categories',views.CategoryList.as_view()),
    path('product_variation_options', views.ProductVariationOptionList.as_view()),
    path('product_variation_options/<int:pk>', views.ProductVariationOptionList.as_view()),
    path('extras', views.ExtraList.as_view()),
    path('extras/<int:pk>', views.ExtraDetail.as_view()),
]
