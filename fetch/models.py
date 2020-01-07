from django.db import models

# Create your models here.
class year(models.Model):
	year = models.IntegerField(primary_key = True)