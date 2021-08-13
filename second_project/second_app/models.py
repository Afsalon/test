from django.db import models

# Create your models here.
class Userid(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    email = models.EmailField()
