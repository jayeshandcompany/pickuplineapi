from django.db import models


# Create your models here.
class pickuplines(models.Model):
  id = models.AutoField(primary_key=True)
  pickupline = models.CharField(max_length=200)
