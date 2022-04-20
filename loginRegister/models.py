from operator import truediv
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email= models.EmailField(unique=True, null= True)
    address=models.CharField(max_length=100, null= True)
    city =models.CharField(max_length=100, null= True)
    province_number=models.IntegerField(max_length=2, null=True)
    zip_code=models.IntegerField(max_length=10, null=True)
    phone=models.IntegerField(max_length=13, null=True)
    
    REQUIRED_FIELDS =[]
    
    