from django.db import models

# Create your models here.


class Person(models.Model):
    """Model represnting a person object"""

    name = models.CharField(unique=True)
    id = models.AutoField(unique=True, primary_key=True)
