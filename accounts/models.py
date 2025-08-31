from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # Add the full name field which is required 
    # in addition to django's default email and password fields
    full_name = models.CharField(
        max_length=255, 
    )
    
    def __str__(self):
        # Returns the user's email as an identifier 
        # during object queries in the terminal
        return self.email  



