from django.db import models

# Create your models here.

class DateModel(models.Model):

    start_date=models.DateField()
    end_date=models.DateField()





