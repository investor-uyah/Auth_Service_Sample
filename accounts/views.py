from rest_framework import generics
from .serializers import RegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Create your views here. 

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer # Name of serializer to be used in the view


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['full_name'] = user.full_name
        return token

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer