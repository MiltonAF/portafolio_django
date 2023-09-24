from django.db import models
import datetime

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/img')
    date = models.DateField(datetime.date.today)