from django.db import models


# Create your models here.

class Head(models.Model):
    hi = models.CharField(max_length=30, null=False)
    about = models.TextField(max_length=200, null=False)
    button = models.CharField(max_length=10, null=False)
    fullname = models.CharField(max_length=30, null=False)
