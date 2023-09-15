from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User

class Result(models.Model):
    user = models.CharField(max_length=255)
    category = models.IntegerField()
    seconds = models.IntegerField()
