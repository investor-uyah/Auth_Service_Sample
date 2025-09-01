from django.http import HttpResponse
from django.urls import path
from .views import RegistrationView, LoginView


# Create your views here. 


def home(request):
    return HttpResponse("Django Auth Service is live. Try '/auth/login' or '/auth/register' or 'api/password_reset' to see available pages.")


urlpatterns = [
    path('', home),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]