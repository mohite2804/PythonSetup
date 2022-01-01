from django.db import models
from django.utils import timezone
from datetime import datetime

class stock(models.Model):
 
  name = models.CharField(max_length = 50,default='',null=True)
  stock_exchange = models.CharField(max_length = 50,default='',null=True)
  strike_price_gap = models.CharField(max_length = 50,default='',null=True)
  is_active =  models.IntegerField(default='1')
  created_by =  models.IntegerField(default='1')
  updated_by =  models.IntegerField(default='1')
  created_at =  models.DateTimeField(default=timezone.now)
  


  class Meta:
    db_table = "stocks"
