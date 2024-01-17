# your_app_name/models.py
from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class signup(models.Model):
    serial_no = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.serial_no} - {self.username}"
    
    def save(self, *args, **kwargs):
        # Hash the password before saving it to the database
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        # Check if the provided password matches the hashed password
        return check_password(raw_password, self.password)