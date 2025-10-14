from django.db import models

# Create your models here.
class Geekmodels(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.TextField(default="None")

    def __str__(self):
        return self.name
