from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


from django.core.exceptions import ValidationError


def validate_cin(value):
    if len(value) != 8 :
        
        raise ValidationError("cin must has 8 characters")


def validate_email(value):
    if str(value).endswith('@esprit.tn') == False:
        
        raise ValidationError("your email must end with @esprit.tn")

class Person(AbstractUser):
    cin = models.CharField(max_length=8 , primary_key=True , validators=[validate_cin])
    email = models.EmailField(max_length=20 , validators=[validate_email])
    username = models.CharField(max_length=20 , unique=True)
    
    USERNAME_FIELD="username"
    
    
    class Meta:
        verbose_name="Person"