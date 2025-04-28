from django.db import models
import random
import string
def account_no_generator():
    prefix = '00'
    rand = ''.join(random.choices(string.digits,k=10))
    return prefix+rand

class Accounts(models.Model):
    id = models.BigAutoField(primary_key=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    savings_account = models.CharField(
        max_length=25,
        unique=True,
        editable=False,
        default=account_no_generator
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ledgers(models.Model):
   id = models.BigAutoField(primary_key=True)
   current = models.DecimalField(max_digits=10,decimal_places=2,default=0)
   hold = models.DecimalField(max_digits=10, decimal_places=2,default=0)
   account_no = models.ForeignKey(Accounts,on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   @property
   def available(self):
       return self.current - self.hold
