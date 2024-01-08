from django.db import models
from django.core.validators import MaxValueValidator
 
class service (models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    sub1 = models.IntegerField(validators=[MaxValueValidator(99)])
    sub2 = models.IntegerField(validators=[MaxValueValidator(99)])
    sub3 = models.IntegerField(validators=[MaxValueValidator(99)])
    sub4 = models.IntegerField(validators=[MaxValueValidator(99)])
    sub5 = models.IntegerField(validators=[MaxValueValidator(99)])



# Create your models here.

