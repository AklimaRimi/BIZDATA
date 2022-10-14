from operator import delitem
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class csvfiles(models.Model):
    Invoice_ID                  = models.CharField(max_length = 200)
    Branch                      =  models.CharField(max_length = 200)
    City                        =models.CharField(max_length = 200)
    Customer_type               =models.CharField(max_length = 200)
    Gender                      =models.CharField(max_length = 200)
    Product_line                =models.CharField(max_length = 200)
    Unit_price                  = models.FloatField()
    Quantity                    = models.IntegerField()
    Tax_5pct                    = models.FloatField()
    Total                       =models.FloatField()
    Date                        =models.CharField(max_length = 200)
    Time                        =models.CharField(max_length = 200)
    Payment                     =models.CharField(max_length = 200)
    cogs                        =models.FloatField()
    gross_margin_percentage     =models.FloatField()
    gross_income                =models.FloatField()
    Rating                      =models.FloatField()
    
class new_data(models.Model):
    date = models.CharField(max_length = 200)
    gross_income = models.FloatField()
