from django.db import models

# Create your models here.


class Signup_user(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    mobile=models.IntegerField(max_length=10)

    