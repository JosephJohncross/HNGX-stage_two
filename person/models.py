from django.db import models

# Create your models here.


class Person(models.Model):
    """Model represnting a person object"""

    name = models.CharField(unique=True, max_length=255)
    id = models.AutoField(primary_key=True)
