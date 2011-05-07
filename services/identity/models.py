import arkpy
from django.db import models


class Identifier(models.Model):
    name = models.CharField(max_length=32, unique=True)
