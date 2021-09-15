
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
import logging
from django.contrib.auth import get_user_model


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        
        data['id'] = self.user.id
        data['email'] = self.user.email
        # data['first_name'] = self.user.first_name
        # data['last_name'] = self.user.last_name
        # data['image'] = self.user.image
        # data['contact_phone'] = self.user.contact_phone
        # data['is_superuser'] = self.user.is_superuser
        # data['is_staff'] = self.user.is_staff
        # data['date_joined'] = self.user.date_joined
        # data['groups'] = self.user.groups
        # data['user_permissions'] = self.user.user_permissions
        return data