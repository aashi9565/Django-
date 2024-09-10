from django.db import models

# Create your models here.



class signup_data(models.Model):
    fname=models.CharField(max_length=200,default="")
    lname=models.CharField(max_length=200,default="")
    email=models.CharField(max_length=200,default="")
    password=models.CharField(max_length=200,default="")



    def __str__(self):
        return self.fname+self.lname+self.email+self.password