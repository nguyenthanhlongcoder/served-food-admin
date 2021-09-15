from django.urls import path
from users.views import UserList, UserDetail
from .views import MyTokenObtainPairView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>', UserDetail.as_view()),
    path('login/',MyTokenObtainPairView.as_view(), name='login'),

]
