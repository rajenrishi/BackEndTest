from django.db import models

# Create your models here.
class ExRate(models.Model):
    ex_rate = models.CharField(max_length=50, blank=True)
    lst_refreshed_ts = models.CharField(max_length=100, blank=True)
