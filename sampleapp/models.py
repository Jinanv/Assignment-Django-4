from django.db import models

# Create your models here.

class log (models.Model):
    username=models.CharField(max_length=50,null=True)
    age = models.IntegerField()
    email = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200,null=True)
    conform_password = models.CharField(max_length=200,null=True)

class reg (models.Model):
    username=models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=200,null=True)