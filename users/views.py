from django.shortcuts import render
from knox.models import AuthToken
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from users import serializers
from datetime import timedelta
from django.utils import timezone
from django.conf import settings
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    
class LoginAPI(generics.GenericAPIView):
    serializer_class = serializers.LoginUserSerializer

    def expires_in(token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        
        return Response({
            "user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })