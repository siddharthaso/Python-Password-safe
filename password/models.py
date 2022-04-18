from pyexpat import model
from django.db import models

# Create your models here.
class password(models.Model):
    password_description = models.TextField()

    def __str__(self):
        return self.password_description