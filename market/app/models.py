from django.db import models

# Create your models here.

class Data(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=255)
    high = models.CharField(max_length=255)
    low = models.CharField(max_length=255)
    open = models.CharField(max_length=255)
    close = models.CharField(max_length=255)
    volume = models.CharField(max_length=255)

    class Meta:
        db_table = "Data"
    