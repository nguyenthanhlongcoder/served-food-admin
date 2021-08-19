from django.urls import path
from . import views
from knox import views as knox_views
from .views import LoginAPI

urlpatterns = [
    path('', views.UserList.as_view()),
    path('<int:pk>', views.UserDetail.as_view()),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
