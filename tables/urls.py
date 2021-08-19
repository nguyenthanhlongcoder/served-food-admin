from django.urls import path
from . import views

urlpatterns = [
    path('', views.TableList.as_view()),
    path('<int:pk>', views.TableDetail.as_view()),
]
