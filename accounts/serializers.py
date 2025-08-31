from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        # specifies the model applied
        model = User

        # specifies the fields to be accepted 
        fields = ('full_name', 'email', 'password')

        # specifies that the password input 
        #should not be passed across the serializer
        extra_kwags = {'password': {'write_only': True}}
    
    # This line allows for creation of new user objects
    def create(user, validated_data): 
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            full_name=validated_data['full_name']
        )
        return user


class LoginSerializer(TokenObtainPairSerializer):
    # Use the default email and password verification from this serializer
    pass 