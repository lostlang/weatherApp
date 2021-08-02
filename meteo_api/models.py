from django.db import models

# Create your models here.


class Log(models.Model):
    date = models.DateField('Date request')
    time = models.TimeField('Time request')
