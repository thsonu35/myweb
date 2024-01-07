from django.db import models
 
class service (models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
# Create your models here.
