from django.db import models

# Create your models here.
class admin_model(models.Model):
    role = models.CharField(max_length=70),
    
