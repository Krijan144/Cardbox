from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SignupModel(models.Model):
 username = models.CharField(max_length=20)
 email = models.EmailField(max_length=200)
 password = models.CharField(max_length=20)
 phone = models.IntegerField(max_length=20)
 image = models.ImageField()
 bio = models.CharField(max_length=200)


