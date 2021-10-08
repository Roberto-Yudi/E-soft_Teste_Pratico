from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False)
    idade = models.PositiveIntegerField(null=True, blank=False)
    nascimento = models.DateField(null=True, blank=False)
    apelido = models.CharField(max_length=80,null=True, blank=True)
    observação = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

