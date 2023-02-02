from django.db import models

# Create your models here.
class Coffee(models.Model):
    fname = models.CharField(max_length=1000)
    sname = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    amount = models.CharField(max_length=1000)
    quantity = models.CharField(max_length=1000)
    payment_id = models.CharField(max_length=1000)
    Paid = models.BooleanField(default=False)
    

    


